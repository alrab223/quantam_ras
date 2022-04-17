import numpy as np
import cv2
from matplotlib import pyplot as plt

# 画像から輪郭を検出する関数


class Tracking():

   def __init__(self, file_name):
      self.x_list = []
      self.y_list = []
      self.movie = cv2.VideoCapture(file_name)
      self.fps = int(self.movie.get(cv2.CAP_PROP_FPS))
      self.w = int(self.movie.get(cv2.CAP_PROP_FRAME_WIDTH))
      self.h = int(self.movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
      self.fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
      self.video = cv2.VideoWriter('video_out2.mp4', self.fourcc, self.fps, (self.w, self.h), True)

   def contours(self, img):
      img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      ret, img_binary = cv2.threshold(img_gray,
                                      60, 255,
                                      cv2.THRESH_BINARY)
      contours, hierarchy = cv2.findContours(img_binary,
                                             cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)
      contours = np.array(contours)
      x = np.mean(contours[0].T[0, 0])
      y = np.mean(contours[0].T[1, 0])
      return x, y

   def marking(self, frame):
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      _, frame = cv2.threshold(frame, 30, 155, cv2.THRESH_BINARY_INV)
      M = cv2.moments(frame)
      if M['m00'] != 0:
         cx = int(M['m10'] / M['m00'])
         cy = int(M['m01'] / M['m00'])
      else:
         cx = int(frame.shape[1] / 2)
         cy = int(frame.shape[0] / 2)
         return frame, None, None
      cv2.line(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)), (cx, cy), (59, 195, 105), 3)
      cv2.drawMarker(frame, (cx, cy), color=(57, 87, 255), markerType=cv2.MARKER_STAR, thickness=2)
      diff_cx = cx - int(frame.shape[1] / 2)
      diff_cy = cy - int(frame.shape[0] / 2)
      return frame, cx, cy

   def cut(self, frame):
      x, y = frame.shape[1] // 4, frame.shape[0] // 4
      h, w = frame.shape[0] // 2, frame.shape[1] // 2
      frame = frame[y:y + h, x:x + w]
      return frame

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

   def main(self):
      while True:
         ret, frame = self.movie.read()
         if not ret:
            break
         frame, cx, cy = self.marking(frame)
         cv2.imshow("title", frame)
         if cv2.waitKey(1) & 0xFF == ord('q'):
            break
         self.video.write(frame)
         self.x_list.append(cx)
         self.y_list.append(cy)

      print("読み込み完了")
      self.movie.release()
      self.graph_maker()


if __name__ == '__main__':
   cam = Tracking(0)
   cam.main()
