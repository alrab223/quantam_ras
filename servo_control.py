import pigpio
import time
import math


class Servo:

   def __init__(self):
      self.servo1 = 2
      self.servo2 = 12
      self.servo3 = 26
      self.pi = pigpio.pi()
      self.servo1_pwm = 1500  # 停止値の指定
      self.servo2_pwm = 1500  # 停止値の指定
      self.servo3_pwm = 1500  # 停止値の指定
      self.omni1_angle = 270
      self.omni2_angle = 30
      self.omni3_angle = 150
      self.speed = 120  # パルス幅の指定-500~500
      self.pi.set_mode(self.servo1, pigpio.OUTPUT)
      self.pi.set_mode(self.servo2, pigpio.OUTPUT)
      self.pi.set_mode(self.servo3, pigpio.OUTPUT)

   def angle_control(self, angle):
      Vx = math.cos(math.radians(angle))
      Vy = math.sin(math.radians(angle))
      coefficient1 = round(Vx * math.cos(math.radians(self.omni1_angle)) + Vy * math.sin(math.radians(self.omni1_angle)), 6)
      coefficient2 = round(Vx * math.cos(math.radians(self.omni2_angle)) + Vy * math.sin(math.radians(self.omni2_angle)), 6)
      coefficient3 = round(Vx * math.cos(math.radians(self.omni3_angle)) + Vy * math.sin(math.radians(self.omni3_angle)), 6)
      return coefficient1, coefficient2, coefficient3

   def rotation_control(self, angle):
      self.pi.set_servo_pulsewidth(self.servo1, self.servo1_pwm + angle[0])
      self.pi.set_servo_pulsewidth(self.servo2, self.servo2_pwm + angle[1])
      self.pi.set_servo_pulsewidth(self.servo3, self.servo3_pwm + angle[2])

   def stop(self):
      self.pi.set_servo_pulsewidth(self.servo1, self.servo1_pwm)
      self.pi.set_servo_pulsewidth(self.servo2, self.servo2_pwm)
      self.pi.set_servo_pulsewidth(self.servo3, self.servo3_pwm)

   def rotation(self, optional_angle, sec):  # 360°回転するまでループ
      for i in range(0, 360, optional_angle):
         angle = self.angle_control(i)
         angle = [x * self.speed for x in angle]
         self.rotation_control(angle)
         time.sleep(sec)

   def main(self):
      time.sleep(3)
      while True:
         self.rotation(90, 1)  # 進行角度と進行持続時間を指定
      self.pi.stop()


if __name__ == '__main__':
   servo = Servo()
   servo.main()
