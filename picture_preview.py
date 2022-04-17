from udp_client import QuANTAM_CAMERA
cam = QuANTAM_CAMERA()
import cv2
while True:
   ret, frame = cam.read()  
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
      break