from socket import socket, AF_INET, SOCK_DGRAM
import cv2
import numpy as np
import base64
import datetime
PORT = 8000
ADDRESS = "192.168.0.21" # 自分に送信

s = socket(AF_INET, SOCK_DGRAM)

while True:
    s.sendto("%.6f" % time.time(),(ADDRESS,PORT))

s.close()