from socket import socket, AF_INET, SOCK_DGRAM
import numpy as np
import cv2
import time
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
         now="%.6f" % time.time()
         print(str(float(now) - float(msg)))
         
      udp.close()

   def socket_server_up(self):
      udp = socket(AF_INET, SOCK_DGRAM)
      udp.bind((self.host, self.port))
      print(udp)
      self.send_message(udp)
      
if __name__ == '__main__':
   client = SocketServer()
   client.socket_server_up()