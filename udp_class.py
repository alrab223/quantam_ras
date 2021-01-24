from socket import socket, AF_INET, SOCK_DGRAM
import numpy as np
import cv2

class SocketServer():
   def __init__(self):
      self.host = '192.168.0.21'   
      self.port = 8000
      self.buffer = 2048
      self.SCALED_IMG_SIZE=512

   def send_message(self, udp):
      while True:
         msg, address = udp.recvfrom(self.buffer)
         img_array = np.frombuffer(msg, dtype=np.uint8)
         img_from_text = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
         img_from_text=cv2.resize(img_from_text, (self.SCALED_IMG_SIZE, self.SCALED_IMG_SIZE), interpolation=cv2.INTER_LANCZOS4)
         _, frame = cv2.threshold(img_from_text, 100, 255, cv2.THRESH_BINARY)
         cv2.imshow('frame',img_from_text)
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