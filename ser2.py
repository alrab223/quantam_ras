import pigpio
import time
import math


class Servo():

   def __init__(self):
<<<<<<< HEAD
      self.servo1 = 2  # 緑ケーブル
      self.servo2 = 12  # 前転に難あり、紫ケーブル
      self.servo3 = 26
=======
      self.servo1 = 2#緑ケーブル
      self.servo2 = 12#前転に難あり、紫ケーブル
      self.servo3=26
>>>>>>> 96355fed7ffbd77259ade99dae49d3c8de5bbe89
      self.pi = pigpio.pi()
      self.servo1_pwm = 1500
      self.servo2_pwm = 1500
      self.servo3_pwm = 1500
<<<<<<< HEAD
      self.servo1_angle = 90
      self.servo2_angle = 210
      self.servo3_angle = 330
      self.pi.set_mode(self.servo1, pigpio.OUTPUT)
      self.pi.set_mode(self.servo2, pigpio.OUTPUT)
      self.pi.set_mode(self.servo3, pigpio.OUTPUT)

   def angle_control(self, angle):
      coefficient1 = math.cos(math.radians(angle - self.servo1_angle)) * (-1)
      coefficient2 = math.cos(math.radians(angle - self.servo2_angle)) * (-1)
      coefficient3 = math.cos(math.radians(angle - self.servo3_angle)) * (-1)
      print(coefficient1, coefficient2, coefficient3)

=======
      self.pi.set_mode(self.servo1, pigpio.OUTPUT)
      self.pi.set_mode(self.servo2, pigpio.OUTPUT)
      self.pi.set_mode(self.servo3, pigpio.OUTPUT)
   
>>>>>>> 96355fed7ffbd77259ade99dae49d3c8de5bbe89
   def go_ahed(self):
      self.pi.set_servo_pulsewidth(self.servo1, 1380)
      self.pi.set_servo_pulsewidth(self.servo2, 1620)
      self.pi.set_servo_pulsewidth(self.servo3, 1600)
<<<<<<< HEAD

=======
   
>>>>>>> 96355fed7ffbd77259ade99dae49d3c8de5bbe89
   def go_ahed_super(self):
      self.pi.set_servo_pulsewidth(self.servo1, 1200)
      self.pi.set_servo_pulsewidth(self.servo2, 1200)
      self.pi.set_servo_pulsewidth(self.servo3, 1200)
<<<<<<< HEAD

=======
   
>>>>>>> 96355fed7ffbd77259ade99dae49d3c8de5bbe89
   def go_ahed_slow(self):
      self.pi.set_servo_pulsewidth(self.servo1, 1550)
      self.pi.set_servo_pulsewidth(self.servo2, 1450)
      self.pi.set_servo_pulsewidth(self.servo3, 1450)
<<<<<<< HEAD

=======
   
>>>>>>> 96355fed7ffbd77259ade99dae49d3c8de5bbe89
   def go_back(self):
      self.pi.set_servo_pulsewidth(self.servo1, 1600)
      self.pi.set_servo_pulsewidth(self.servo2, 1400)
      self.pi.set_servo_pulsewidth(self.servo3, 1400)
<<<<<<< HEAD

=======
   
>>>>>>> 96355fed7ffbd77259ade99dae49d3c8de5bbe89
   def go_back_slow(self):
      self.pi.set_servo_pulsewidth(self.servo1, 1550)
      self.pi.set_servo_pulsewidth(self.servo2, 1450)
      self.pi.set_servo_pulsewidth(self.servo3, 1420)
<<<<<<< HEAD

=======
   
>>>>>>> 96355fed7ffbd77259ade99dae49d3c8de5bbe89
   def go_right_up(self):
      self.pi.set_servo_pulsewidth(self.servo1, 1500)
      # self.pi.hardware_PWM(self.servo2,50,77500)
      self.pi.set_servo_pulsewidth(self.servo2, 1620)
      self.pi.set_servo_pulsewidth(self.servo3, 1400)

   def stop(self):
      self.pi.set_servo_pulsewidth(self.servo1, 1500)
      self.pi.set_servo_pulsewidth(self.servo2, 1500)
      self.pi.set_servo_pulsewidth(self.servo3, 1500)
<<<<<<< HEAD

=======
   
>>>>>>> 96355fed7ffbd77259ade99dae49d3c8de5bbe89
   def debug(self):
      self.pi.set_servo_pulsewidth(self.servo1, 1300)
      # self.pi.hardware_PWM(self.servo2,50,77500)
      self.pi.set_servo_pulsewidth(self.servo2, 1700)
      self.pi.set_servo_pulsewidth(self.servo3, 1700)

<<<<<<< HEAD
   def debug_rotation(self, num):
      self.pi.set_servo_pulsewidth(self.servo1, 1500 + num)
      self.pi.set_servo_pulsewidth(self.servo2, 1500 + num)
      self.pi.set_servo_pulsewidth(self.servo3, 1500 + num)

   def main(self):
      while True:
         self.angle_control(90)

      self.pi.stop()


=======
   def debug_rotation(self,num):
      self.pi.set_servo_pulsewidth(self.servo1, 1500+num)
      self.pi.set_servo_pulsewidth(self.servo2, 1500+num)
      self.pi.set_servo_pulsewidth(self.servo3, 1500+num)
 
   def main(self):
      while True:
         self.debug()
         time.sleep(3)
         self.stop()
         time.sleep(3)


      self.pi.stop()
>>>>>>> 96355fed7ffbd77259ade99dae49d3c8de5bbe89
if __name__ == '__main__':
   servo = Servo()
   servo.main()
