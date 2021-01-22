import io
import cv2
import base64
import numpy as np
#バイナリにしたい画像を読み込み
import socket


## UDP送信クラス
class udpsend():
    def __init__(self):

        SrcIP = "192.168.0.13"                        
 
    def send(self):
        capture = cv2.VideoCapture(0)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('192.168.0.8', 8000))
            while True:
                _, frame = capture.read()
                _, buffer = cv2.imencode('.jpg', frame)
                img_as_text = base64.b64encode(buffer).decode('utf-8')
                img_binary = base64.b64decode(img_as_text.encode('utf-8'))
                s.sendall(img_binary)
                
udp = udpsend()     # クラス呼び出し
udp.send()          # 関数実行

