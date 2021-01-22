from socket import socket, AF_INET, SOCK_DGRAM
import numpy as np
import cv2
HOST = '192.168.0.21'   
PORT = 8000

# ソケットを用意
s = socket(AF_INET, SOCK_DGRAM)
# バインドしておく
s.bind((HOST,PORT))

while True:
    # 受信
    msg, address = s.recvfrom(2048)
    img_array = np.frombuffer(msg, dtype=np.uint8)
    img_from_text = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    _, frame = cv2.threshold(img_from_text, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow('frame',img_from_text)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ソケットを閉じておく
s.close()