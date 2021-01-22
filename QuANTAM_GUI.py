# -*- coding: utf-8 -*-
import gui #QtDesignerで作った画面をインポートする

import ast
import os
import sys
import csv
import datetime

from PyQt5.QtCore import QPoint, Qt, QCoreApplication, pyqtSignal, QMutexLocker, QMutex, QThread, QTimer
from PyQt5.QtGui import(QIcon, QImage, QPixmap, QPainter, QColor, QKeySequence, QPalette, QFont)
from PyQt5.QtWidgets import *
from PyQt5.QtTest import *
import time
import socket
import numpy as np
import cv2

SCALED_IMG_SIZE = 560

class Worker(QThread):
    """
    画像をUDPで受け取り、制御信号をSpresenseに送り返すスレッド
    sig_imageシグナルを発行しPC側でのプレビューも行う
    """

    sig_images = pyqtSignal(QPixmap, QPixmap)

    def __init__(self, widget, server_ip, main):
        time.sleep(0.5)
        super(QThread, self).__init__()

        self.threshold = 100
        self.init = False
        self.ui_widget = widget
        self.server_ip = server_ip
        self.server_port = 5000
        self.sending = False
        self.main_window = main

        self.activate = True
        self.csvrec = False
        self.shutter = False

        self.pwm_range = 80
        
    def create_Qpixmap_from_ndarray(self, ndarray_bgr_img):
        """
        BGR形式のndarrayデータをQpixmapに変換
        """
        height, width, channel = ndarray_bgr_img.shape
        bytesPerLine = 3 * width
        qImg = QImage(ndarray_bgr_img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        qPixelmap = QPixmap(qImg) 
        
        return qPixelmap

    def run(self):
        """
        QThread.start()で開始すると実行される関数
        """
        print("worker started")

        time.sleep(0.1) #server_ip_labelで強制終了してしまうことがあるため

        #ステータス情報
        self.ui_widget.host_name_label.setText( socket.gethostname() )
        self.ui_widget.server_ip_label.setText(self.server_ip)
        
        #PID制御用
        self.Kp_dist = 1
        self.Kd_dist = 0
        self.pre_error_xerror_x = 0
        self.pre_error_xerror_y = 0
        self.integ_error_x = 0
        self.integ_error_y = 0
        self.diff_error_x = 0
        self.diff_error_y = 0

        #PID制御 角度
        self.Kp_angle = 1
        self.Kd_angle = 0
        self.pre_error_xerror_angle = 0
        self.diff_error_angle = 0
        self.cos = 0.0
        self.a_dist = 0 #角度の補正値の距離に関する比例定数の倍率

        self.last_draw_sec = 0
        self.do_refresh = False

        #イベントにスロットを設定

        self.ui_widget.csv_button.toggled.connect(self.csv_change)
        self.ui_widget.camera_button.toggled.connect(self.camera_change)


        self.ui_widget.threshold_slider.valueChanged.connect(self.change_threshold)
        self.ui_widget.send_checkbox.stateChanged.connect(self.change_sendsignal)

        self.ui_widget.k_p_spinbox.setValue(self.Kp_dist)
        self.ui_widget.k_d_spinbox.setValue(self.Kd_dist)

        self.ui_widget.k_p_spinbox.valueChanged.connect(self.change_k_p)
        self.ui_widget.k_d_spinbox.valueChanged.connect(self.change_k_d)

        self.ui_widget.k_p_spinbox_angle.setValue(self.Kp_angle)
        self.ui_widget.k_d_spinbox_angle.setValue(self.Kd_angle)

        self.ui_widget.k_p_spinbox_angle.valueChanged.connect(self.change_k_p_angle)
        self.ui_widget.k_d_spinbox_angle.valueChanged.connect(self.change_k_d_angle)

        self.ui_widget.a_dist_spinbox.valueChanged.connect(self.change_a_dist)

        self.last_sec = 0

        self.main_window.timer.timeout.connect(self.receive_image)

    def receive_image(self):
        # print("[CAL]receive_image", time.perf_counter())
        while not self.activate:
            continue
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.server_ip, self.server_port))

        #受信し終わってから次の待受までの時間（OpenCVの処理時間）
        # time_delta = time.perf_counter() - self.last_sec
        # self.ui_widget.opencv_time_label.setNum(time_delta)
        # self.last_sec = time.perf_counter()
    

        data, addr = sock.recvfrom(1024)
        # 初回受信時はSpresenseのIPアドレスを表示する
        if not self.init:
            self.ui_widget.address_label.setText( addr[0] )
            self.init = True

        #バーとかラベルの更新頻度
        if time.perf_counter() - self.last_draw_sec > 0.1:
            self.do_refresh = True
            self.last_draw_sec = time.perf_counter()
        else:
            self.do_refresh = False

        #待受が終わるまでの時間（受信にかかる時間）
        # time_delta = time.perf_counter() - self.last_sec
        # self.ui_widget.receive_time_label.setNum(time_delta)
        # self.last_sec = time.perf_counter()
        # if time_delta < 0.03:
        #     print("skip")
        #     continue

        # 送信されてきたバイナリデータを画像として変換
        gray_img = np.frombuffer(data, dtype=np.uint8)
        gray_img = np.reshape(gray_img, (28, 28))

        # 拡大処理を行う　補間方法の他には cv2.INTER_LANCZOS4 cv2.INTER_NEAREST などがある
        gray_img_resized = cv2.resize(gray_img, (SCALED_IMG_SIZE, SCALED_IMG_SIZE), interpolation=cv2.INTER_LANCZOS4)
        ret, binary_img = cv2.threshold(gray_img_resized, self.threshold, 255, cv2.THRESH_BINARY_INV) #2値化（背景が黒, 物体が白になるよう反転)

        #PID制御
        M = cv2.moments(binary_img)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx = int(SCALED_IMG_SIZE / 2)
            cy = int(SCALED_IMG_SIZE / 2)

        # ---------------------------- 画面中心からの誤差
        error_x = cx - int(SCALED_IMG_SIZE / 2)
        error_y = cy - int(SCALED_IMG_SIZE / 2)

        # ---------------------------- 距離の誤差から補正値を計算

        self.diff_error_x = self.pre_error_xerror_x - error_x
        self.diff_error_y = self.pre_error_xerror_y - error_y
        self.integ_error_x = self.integ_error_x + error_x /280
        self.integ_error_y = self.integ_error_y + error_y /280
        # self.ui_widget.integ_error_x_label.setNum(self.integ_error_x)
        # self.ui_widget.integ_error_y_label.setNum(self.integ_error_y)

        # 距離の補正値（両輪同じ値）
        dist_ctrl_left = - (self.Kp_dist * error_y - self.Kd_dist * self.diff_error_y)
        if self.do_refresh:
            self.ui_widget.distance_value_bar_left.setValue(dist_ctrl_left)
            self.ui_widget.distance_value_label_left.setNum(dist_ctrl_left)

        dist_ctrl_right = - (self.Kp_dist * error_y - self.Kd_dist * self.diff_error_y)
        if self.do_refresh:
            self.ui_widget.distance_value_bar_right.setValue(dist_ctrl_right)
            self.ui_widget.distance_value_label_right.setNum(dist_ctrl_right)

        self.pre_error_xerror_x = error_x
        self.pre_error_xerror_y = error_y

        # ---------------------------- 角度の誤差から補正値を計算
        front_vec = np.array([0, 1])
        musi_vec = np.array([error_x, -error_y])
        musi_dist = np.linalg.norm(musi_vec)

        inner = np.inner(front_vec, musi_vec) #内積
        norm = np.linalg.norm(front_vec) * np.linalg.norm(musi_vec) #ベクトルの長さ
        print(inner)

        if norm != 0:
            self.cos = inner / norm
            angle = np.rad2deg(np.arccos(np.clip(self.cos, -1.0, 1.0)))
        else:
            angle = 0

        #angleは正負がないため、error_xを見て符号をつける
        if error_x < 0:
            angle = -angle

        #ダンゴムシがカメラの下半分に来たとき
        if angle > 90: #右下
            angle = 180 - angle
            angle = -angle
        elif angle < - 90: #左下
            angle = - 180 - angle
            angle = -angle



        self.diff_error_angle = self.pre_error_xerror_angle - angle
        self.pre_error_xerror_angle = angle

        angle_ctrl_left = -(self.Kp_angle * angle - self.Kd_angle * self.diff_error_angle)
        angle_ctrl_left *= abs(musi_dist) / 280 #距離の誤差に比例させる
        if self.do_refresh:
            self.ui_widget.angle_value_bar_left.setValue(int(angle_ctrl_left))
            self.ui_widget.angle_value_label_left.setNum(int(angle_ctrl_left))

        angle_ctrl_right = self.Kp_angle * angle - self.Kd_angle * self.diff_error_angle
        angle_ctrl_right *= abs(musi_dist) / 280 #距離の誤差に比例させる
        if self.do_refresh:
            self.ui_widget.angle_value_bar_right.setValue(int(angle_ctrl_right))
            self.ui_widget.angle_value_label_right.setNum(int(angle_ctrl_right))


        # ---------------------------- 角度と距離の補正を合成

        sig_L = self.clamp_pwm(angle_ctrl_left + dist_ctrl_left)
        sig_R = self.clamp_pwm(angle_ctrl_right + dist_ctrl_right)

        #ここでCSVに保存
        self.ui_widget.process_time.setNum(time.perf_counter())
        if self.csvrec:
            self.writer.writerow([str(time.perf_counter()), error_x, error_y, abs(musi_dist), angle, sig_L, sig_R, self.Kp_dist, self.Kd_dist, self.Kp_angle, self.Kd_angle])

        if self.ui_widget.manual_button.isChecked():
            sig_L = self.clamp_pwm(self.ui_widget.test_left_spinbox.value())
            sig_R = self.clamp_pwm(self.ui_widget.test_right_spinbox.value())

        if self.do_refresh:
            self.ui_widget.signal_left_bar.setValue(sig_L)
            self.ui_widget.signal_right_bar.setValue(sig_R)

        ctrl_signal = str(sig_L) + "," + str(sig_R)
        print("ctrl_signal:", ctrl_signal)

        # ---------------------------- 信号送信

        if self.shutter:
            self.shutter = False
            signal_utf8 = str("300,300").encode('utf-8')
            sock.sendto(signal_utf8, addr)
            self.ui_widget.camera_button.setChecked(False)
        elif self.sending:
            signal_utf8 = str(ctrl_signal).encode('utf-8')
            sock.sendto(signal_utf8, addr)
        else:
            signal_utf8 = "1,1".encode('utf-8')
            sock.sendto(signal_utf8, addr)

        # ---------------------------- プレビュー表示
        if self.ui_widget.preview_button.isChecked():
            #グレースケール画像からRGB画像に変換
            gray_img_resized = cv2.cvtColor(gray_img_resized, cv2.COLOR_GRAY2RGB)
            binary_img = cv2.cvtColor(binary_img, cv2.COLOR_GRAY2RGB)
            
            #マーカー類を描画
            cv2.line(binary_img, (int(SCALED_IMG_SIZE / 2), int(SCALED_IMG_SIZE / 2)), (cx, cy), (59, 195, 105), 3)
            cv2.drawMarker(binary_img, (cx, cy), color=(57, 87, 255), markerType=cv2.MARKER_STAR, thickness=2)

            # PyQtのラベルで表示できる形式QPixmapに変換
            gray_img = self.create_Qpixmap_from_ndarray(gray_img_resized)
            binary_img = self.create_Qpixmap_from_ndarray(binary_img)
            
            self.sig_images.emit(gray_img, binary_img) #画像シグナルを発火
            # print("[END]receive_image", time.perf_counter())
            
        sock.close()

    def change_threshold(self, value):
        self.threshold = value

    def change_sendsignal(self, value):
        # self.sending = v
        if value == 0:
            self.sending = False
        elif value == 2:
            self.sending = True
    
    def change_k_p(self, value):
        self.Kp_dist = value

    def change_k_d(self, value):
        self.Kd_dist = value

    def change_k_p_angle(self, value):
        self.Kp_angle = value

    def change_k_d_angle(self, value):
        self.Kd_angle = value

    def change_a_dist(self, value):
        self.a_dist = value




    def change_start(self, value):
        if value:
            self.ui_widget.start_button.setText('停止')
            self.activate = value
        else:
            self.ui_widget.start_button.setText('開始')
            self.activate = value

    def csv_change(self, value):
        if value:
            print("CSV START")
            filename = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
            self.file = open(filename + '.csv', 'w')
            self.writer = csv.writer(self.file)
            self.writer.writerow(['time', 'error_x', 'error_y', 'target_dist', 'angle', 'sig_L', 'sig_R', 'kp_d',  'kd_d', 'kp_a', 'kd_a'])

            self.ui_widget.csv_button.setText('ファイル停止')
            self.csvrec = value

        else:
            print("CSV END")
            self.file.close()
            self.ui_widget.csv_button.setText('ファイル開始')
            self.csvrec = value

    def camera_change(self, value):
        if value:
            print("shutter")
            self.shutter = True

        else:
            print("no case")


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            print("test")

    def clamp_pwm(self, x):
        """
        xを-255から255の間に制限し、0を1にする
        """
        num = min(self.pwm_range, max(x, -self.pwm_range))
        if num == 0:
            num = 1
        return int(num)


class QuANTAM_Window(QMainWindow):               #QuANTAM_Windowという名前でQMainWindowのサブクラス作成

    def __init__(self, parent=None):        #クラスの初期化

        super().__init__(parent)            #上位クラスの初期化ルーチンを呼び出す（補足2）
        
        self.local_ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
        self.ui = gui.Ui_MainWindow()           #先ほど作ったhello.pyの中にあるクラスの
        self.ui.setupUi(self)               #このコマンドを実行する

        self.a_image = QPixmap(os.path.join(os.getcwd(), 'images', 'dummy_560x560.jpg'))
        self.ui.img1_label.setPixmap(self.a_image)
        self.ui.img2_label.setPixmap(self.a_image)
        
        self.init_worker()
        self.last_sec = 0
        self.fps_count = 0
        self.first_img = 0
        self.second_img = 0

        self.ui.start_button.toggled.connect(self.timer_start)

        self.timer = QTimer()
        
    def timer_start(self, value):
        if value:
            self.timer.start(1000 / 60)
        else:
            self.timer.stop()

    def init_worker(self):
        """
        class Worker(Qthread) のインスタンスを作成し、別スレッドでの映像受信処理を開始する
        """

        self.worker = Worker(self.ui, self.local_ip, self)
        self.worker.sig_images.connect(self.receive_image)
        
        self.worker.start()

    def testfunc(self):
        print("test")

    def receive_image(self, first_img, second_img):
        self.first_img = QPixmap(first_img)
        self.second_img = QPixmap(second_img)

        # ---------------------------- 時間計測
        #毎フレームの時間間隔からFPSを出す方法
        # now_sec = time.perf_counter()
        # time_delta = now_sec - self.last_sec
        # self.last_sec = now_sec
        # self.ui.fps_label.setText( "FPS:{:5.2f}".format(1.0 / time_delta) )

        #１秒間の描画更新回数からFPSを出す方法
        now_sec = time.perf_counter()
        time_delta = now_sec - self.last_sec
        if time_delta >= 0.2:
            self.last_sec = now_sec
            self.ui.fps_label.setText("FPS:{:5.1f}".format(self.fps_count / time_delta))
            self.fps_count = 0
        else:
            self.fps_count += 1

        self.change_image()

        
        # QCoreApplication.processEvents()
    
    def change_image(self):
        self.ui.img1_label.setPixmap(self.first_img)
        self.ui.img2_label.setPixmap(self.second_img)
        self.update()


if __name__ == '__main__':


    app = QApplication(sys.argv)
    
    # Now use a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(55, 55, 55))
    palette.setColor(QPalette.WindowText, Qt.white)
    app.setPalette(palette)

    quantam = QuANTAM_Window()                        #QuANTAM_Windowのインスタンスを作って
    quantam.show()                            #表示する
    sys.exit(app.exec())