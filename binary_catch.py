import socket
import numpy as np
import cv2

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8000))
while True:
    data, addr = sock.recvfrom(302400)
    gray_img = np.frombuffer(data, dtype=np.uint8)
    gray_img = np.reshape(gray_img, (640, 480))
    print(gray_img)