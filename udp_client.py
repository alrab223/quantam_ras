from socket import socket, AF_INET, SOCK_DGRAM,error
import cv2
import numpy as np
import base64
import datetime
import time
import pickle
import asyncio
import select
from contextlib import closing  #with用
from ser2 import Servo
import csv
class QuANTAM_CAMERA:
   def __init__(self):
      self.port = 8000
      self.address = "192.168.0.21"
      self.myaddress = "192.168.0.22" 
      self.cam = cv2.VideoCapture(0)
      self.udp_recive = socket(AF_INET, SOCK_DGRAM)
      self.udp_send = socket(AF_INET, SOCK_DGRAM)
      self.video_capture = False
      self.servo = Servo()
      self.csv_writer=False
   
   def camera_setup(self):
      self.fps = 15
      self.w = 320
      self.h = 240
      self.cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'))
      self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, self.w)
      self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.h)
      self.cam.set(cv2.CAP_PROP_FPS, self.fps)
      self.cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
      
   def record_setup(self):
      
      self.fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
      self.video = cv2.VideoWriter('output2.mp4', self.fourcc, self.fps, (self.w, self.h))
   
   def convert_binary(self, img):
      _, buffer = cv2.imencode('.jpg', img)
      img_as_text = base64.b64encode(buffer).decode('utf-8')
      img_binary = base64.b64decode(img_as_text.encode('utf-8'))
      return img_binary

   def convert_pickle(self, img):
      return pickle.dumps(img, 4)
   
   def record(self, img):
      self.video.write(img)
      
      
   def cam_cap(self):
      self.udp_recive.bind((self.myaddress, self.port))
      self.udp_recive.setblocking(0)
      self.camera_setup()
      if self.video_capture == True:
         self.record_setup()
      print("start")
      with closing(self.udp_send),closing(self.udp_recive):
         while True:
            past=datetime.datetime.now()
            _, frame = self.cam.read()
            if self.video_capture == True:
               self.record(frame)
            frame=cv2.resize(frame,(28,28))
            frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img_binary = self.convert_pickle(frame2)
            self.udp_send.sendto(img_binary, (self.address, self.port))
 
            # try: #try構文内でエラーが起こるとexceptに飛ぶ、なければelseへ
            #    sr, addr = self.udp_recive.recvfrom(1024) #受信する
            # except error: #受信していなければなにもしない
            #    pass
            # else:  #受信していたら表示
            #    if sr == b"go":
            #       self.servo.go_ahed()

            #    else:
            #       self.servo.stop()
quantam = QuANTAM_CAMERA()
quantam.cam_cap()