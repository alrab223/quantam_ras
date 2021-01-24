from socket import socket, AF_INET, SOCK_DGRAM
import cv2
import numpy as np
import base64
import time
PORT = 8000
ADDRESS = "192.168.0.21" # 自分に送信

s = socket(AF_INET, SOCK_DGRAM)
# ブロードキャストする場合は、ADDRESSを
# ブロードキャスト用に設定して、以下のコメントを外す
# s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


capture = cv2.VideoCapture(0)
while True:
    _, frame = capture.read()
    frame=cv2.resize(frame,(28,28))
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, buffer = cv2.imencode('.jpg', frame2)
    img_as_text = base64.b64encode(buffer).decode('utf-8')
    img_binary = base64.b64decode(img_as_text.encode('utf-8'))
    print(frame2.shape)
    s.sendto("%.6f" % time.time(),(ADDRESS,PORT))

s.close()