import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gp_out = 14
gp_out2 = 23
gp_out3 = 18
GPIO.setup(gp_out, GPIO.OUT)
GPIO.setup(gp_out2, GPIO.OUT)
GPIO.setup(gp_out3, GPIO.OUT)
servo = GPIO.PWM(gp_out, 50)
servo2 = GPIO.PWM(gp_out2, 50)
servo3 = GPIO.PWM(gp_out3, 50)
servo.start(7.5)
servo2.start(7.5)
servo3.start(7.5)
time.sleep(2)
# servo.ChangeDutyCycle(5)
# servo2.ChangeDutyCycle(7.5)
# servo3.ChangeDutyCycle(5)
# time.sleep(2)
# servo.ChangeDutyCycle(10)
# servo2.ChangeDutyCycle(10)
# servo3.ChangeDutyCycle(10)
# time.sleep(2)
servo.stop()
GPIO.cleanup() 