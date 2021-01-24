from socket import socket, AF_INET, SOCK_DGRAM
import numpy as np
import cv2
SCALED_IMG_SIZE=512
class SocketServer():
   
   def __init__(self):
      self.host = '192.168.0.21'   
      self.port = 8000
      self.buffer =1024
      self.SCALED_IMG_SIZE = 512
   
   

   def send_message(self, udp):
      while True:
         msg, address = udp.recvfrom(self.buffer)
         img_array = np.frombuffer(msg, dtype=np.uint8)
         img_from_text = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
         frame=cv2.resize(img_from_text, (self.SCALED_IMG_SIZE, self.SCALED_IMG_SIZE), interpolation=cv2.INTER_LANCZOS4)
         # _, frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY_INV)
         x, y = frame.shape[1]//4, frame.shape[0]//4
         h, w = frame.shape[0]*2, frame.shape[1]*2
         frame=frame[y:y+h, x:x+w]
         # M = cv2.moments(frame)
         # if M['m00'] != 0:
         #     cx = int(M['m10']/M['m00'])
         #     cy = int(M['m01']/M['m00'])
         # else:
         #     cx = int(SCALED_IMG_SIZE / 2)
         #     cy = int(SCALED_IMG_SIZE / 2)
         # cv2.line(frame, (int(SCALED_IMG_SIZE / 2), int(SCALED_IMG_SIZE / 2)), (cx, cy), (59, 195, 105), 3)
         # cv2.drawMarker(frame, (cx, cy), color=(57, 87, 255), markerType=cv2.MARKER_STAR, thickness=2)
         cv2.imshow('frame',frame)
         if cv2.waitKey(1) & 0xFF == ord('q'):
            break
      udp.close()

   def socket_server_up(self):
      udp = socket(AF_INET, SOCK_DGRAM)
      udp.bind((self.host, self.port))
      print(udp)
      self.send_message(udp)
      
if __name__ == '__main__':
   client = SocketServer()
   client.socket_server_up()