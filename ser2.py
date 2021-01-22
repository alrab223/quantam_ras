import pigpio
import time

class Servo():

   def __init__(self):
      self.servo1 = 14#SG90HV
      self.servo2 = 18
      self.servo3=23
      self.pi = pigpio.pi()
      self.servo1_pwm = 1500
      self.servo2_pwm = 1500
      self.servo3_pwm=1500
   
   def go_ahed(self):
      self.pi.set_servo_pulsewidth(self.servo1, 1800)
      self.pi.set_servo_pulsewidth(self.servo2, 1400)
      self.pi.set_servo_pulsewidth(self.servo3, 1400)
   
   def go_back(self):
      self.pi.set_servo_pulsewidth(self.servo1, 1200)
      self.pi.set_servo_pulsewidth(self.servo2, 1600)
      self.pi.set_servo_pulsewidth(self.servo3, 1600)
   
   def go_right(self):
      self.pi.set_servo_pulsewidth(self.servo1, 1700)
      self.pi.set_servo_pulsewidth(self.servo2, 1400)
      self.pi.set_servo_pulsewidth(self.servo3, 1400)
 
   def main(self):
      self.pi.set_mode(self.servo1, pigpio.OUTPUT)
      self.pi.set_mode(self.servo2, pigpio.OUTPUT)
      self.pi.set_mode(self.servo3, pigpio.OUTPUT)
      while True:
         self.go_ahed()
         time.sleep(3)
         self.go_back()
         time.sleep(3)    
      self.pi.stop()
servo = Servo()
servo.main()
