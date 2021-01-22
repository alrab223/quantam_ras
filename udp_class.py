from socket import socket, AF_INET, SOCK_DGRAM
import numpy as np
import cv2

class SocketServer():
   def __init__(self):
      self.host = '192.168.0.21'   
      self.port = 8000
      self.buffer=2048

   def socket_server_up(self):
      udp = socket(AF_INET, SOCK_DGRAM)
      
      self.send_message(udp)
   
   def send_message(self, udp):
      udp.bind((self.host, self.port))
      while True:
         msg, address = udp.recvfrom(self.buffer)
         img_array = np.frombuffer(msg, dtype=np.uint8)
         img_from_text = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
         _, frame = cv2.threshold(img_from_text, 100, 255, cv2.THRESH_BINARY)
         cv2.imshow('frame',img_from_text)
         if cv2.waitKey(1) & 0xFF == ord('q'):
            break
      udp.close()
      
if __name__ == "_main_":
   client = SocketServer()
   client.socket_server_up()