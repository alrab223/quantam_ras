import RPi.GPIO as GPIO
import time

class Servo():

   def __init__(self):
      self.servo1 = 2#
      self.servo2 = 12#前転に難あり
      self.servo3=26
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.servo1, GPIO.OUT)
      GPIO.setup(self.servo2, GPIO.OUT)
      GPIO.setup(self.servo3, GPIO.OUT)
      self.servo1_pwm = GPIO.PWM(self.servo1, 50)
      self.servo2_pwm  = GPIO.PWM(self.servo2, 50)
      self.servo3_pwm = GPIO.PWM(self.servo3, 50)
   
   def stop(self):
      self.servo1_pwm.ChangeDutyCycle(7.1)
      self.servo2_pwm.ChangeDutyCycle(7.1)
      self.servo3_pwm.ChangeDutyCycle(7.1)
   
   def debug(self):
      self.servo1_pwm.ChangeDutyCycle(10)
      self.servo2_pwm.ChangeDutyCycle(10)
      self.servo3_pwm.ChangeDutyCycle(10)
    
   def main(self):
      self.servo1_pwm.start(7.1)
      self.servo2_pwm.start(7.1)
      self.servo3_pwm.start(7.1)
      time.sleep(2)
      while True:
         self.debug()
         time.sleep(3)
         self.stop()
         time.sleep(3)

      servo.stop()
      GPIO.cleanup() 
servo = Servo()
servo.main()