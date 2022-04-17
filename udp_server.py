import csv
import math
import pickle
from contextlib import closing  # with用
from socket import AF_INET, SOCK_DGRAM, socket

import cv2
import numpy as np
from matplotlib import pyplot as plt


class SocketServer():

   def __init__(self):
      self.host = '192.168.0.14'
      self.send_host = '192.168.0.28'
      self.port = 8000
      self.buffer = 1024
      self.SCALED_IMG_SIZEX = 520
      self.SCALED_IMG_SIZEY = 520
      self.udp_recive = socket(AF_INET, SOCK_DGRAM)
      self.udp_send = socket(AF_INET, SOCK_DGRAM)
      self.x_list = []
      self.y_list = []
      self.video_capture = False

   def record_setup(self):

      self.fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
      self.video = cv2.VideoWriter('output.mp4', self.fourcc, 15, (self.SCALED_IMG_SIZEX, self.SCALED_IMG_SIZEY), isColor=False)

   def cut(self, frame):
      x, y = frame.shape[1] // 4, frame.shape[0] // 4
      h, w = frame.shape[0] // 2, frame.shape[1] // 2
      frame = frame[y:y + h, x:x + w]
      print(frame.shape)
      return frame

   def marking(self, frame):
      _, frame = cv2.threshold(frame, 30, 155, cv2.THRESH_BINARY_INV)
      M = cv2.moments(frame)
      if M['m00'] != 0:
         cx = int(M['m10'] / M['m00'])
         cy = int(M['m01'] / M['m00'])
      else:
         cx = int(frame.shape[1] / 2)
         cy = int(frame.shape[0] / 2)
      cv2.line(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)), (cx, cy), (59, 195, 105), 3)
      cv2.drawMarker(frame, (cx, cy), color=(57, 87, 255), markerType=cv2.MARKER_STAR, thickness=2)
      return frame, cx, cy

   def graph_maker(self):
      plt.rcParams['font.size'] = 14
      plt.rcParams['font.family'] = 'Times New Roman'

      # 目盛を内側にする。
      plt.rcParams['xtick.direction'] = 'in'
      plt.rcParams['ytick.direction'] = 'in'

      # グラフの上下左右に目盛線を付ける。
      fig = plt.figure()
      ax1 = fig.add_subplot(111)
      ax1.yaxis.set_ticks_position('both')
      ax1.xaxis.set_ticks_position('both')

      # スケール設定
      ax1.set_xlim(0, 400)
      ax1.set_ylim(0, 400)

      # 軸のラベルを設定する。
      ax1.set_xlabel('x')
      ax1.set_ylabel('y')

      # データプロット
      ax1.scatter(self.x_list, self.y_list, label='Tracking result')
      plt.legend()
      fig.tight_layout()

      # グラフを表示する。
      plt.show()
      plt.close()

   def servo_control(self, cx, cy, frame):
      cx = cx - frame.shape[1] / 2
      cy = cy - frame.shape[0] / 2
      if (-10 < cx and 10 > cx) and (-10 < cy and 10 > cy):
         return "stay"
      elif cx == 0 and cy > 10:
         return "270"
      elif cx == 0 and cy < -10:
         return "90"
      elif cy == 0 and cx < -10:
         return "0"
      elif cy == 0 and cx < -10:
         return "180"
      else:
         try:
            if cx > 0:
               angle = round(math.degrees(math.atan(cy / cx))) + 180
            else:
               angle = round(math.degrees(math.atan(cy / cx)) + 360) % 360
            return str(angle)
         except ZeroDivisionError:
            return "stay"

   def send_message(self):
      if self.video_capture:
         self.record_setup()
      with closing(self.udp_recive), closing(self.udp_send):
         while True:
            msg, address = self.udp_recive.recvfrom(self.buffer)
            img_from_text = pickle.loads(msg)
            frame = cv2.resize(
                img_from_text,
                (self.SCALED_IMG_SIZEX,
                 self.SCALED_IMG_SIZEY),
                interpolation=cv2.INTER_LANCZOS4)
            frame = self.cut(frame)
            frame2, cx, cy = self.marking(frame)
            mergeImg = np.hstack((frame, frame2))
            angle = self.servo_control(cx, cy, frame2)
            self.udp_send.sendto(angle.encode(), (self.send_host, self.port))
            if self.video_capture:
               self.video.write(frame2)
            # else:
            #    self.udp_send.sendto(b"stop",(self.send_host,self.port))
            cv2.imshow('frame', mergeImg)
            if cv2.waitKey(1) & 0xFF == ord('q'):
               break
            with open("point2.csv", "a") as f:
               writer = csv.writer(f)
               writer.writerow([cx, cy])
            self.x_list.append(cx)
            self.y_list.append(cy)
         self.graph_maker()
         self.video.release()

   def socket_server_up(self):
      self.udp_recive.bind((self.host, self.port))
      self.send_message()


if __name__ == '__main__':
   client = SocketServer()
   client.socket_server_up()
