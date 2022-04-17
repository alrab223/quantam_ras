from tracking import Tracking
import cv2


class Speed(Tracking):
   def __init__(self, file_name):
      super().__init__(file_name)

   def cam_read(self):
      prex, prey = 0, 0
      while True:
         ret, frame = self.movie.read()
         if not ret:
            break

         frame, cx, cy = self.marking(frame)
         print(cx, cy, cx - prex, cy - prey)
         prex = cx
         prey = cy
         cv2.imshow("title", frame)
         if cv2.waitKey(1) & 0xFF == ord('q'):     # wait for ESC key to exit
            break

         # self.x_list.append(cx)
         # self.y_list.append(cy)
      self.movie.release()


if __name__ == '__main__':
   cam = Speed("frame.mp4")
   cam.cam_read()
