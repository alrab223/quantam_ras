import pigpio
import time


servo2 = 18
servo1 = 14
servo3=23
pi = pigpio.pi()



pi.set_mode(servo1, pigpio.OUTPUT)
pi.set_mode(servo2, pigpio.OUTPUT)
pi.set_mode(servo3, pigpio.OUTPUT)

pi.set_servo_pulsewidth(servo1, 1600)
pi.set_servo_pulsewidth(servo2, 1500)
pi.set_servo_pulsewidth(servo3, 1400)
time.sleep(2)

pi.set_servo_pulsewidth(servo1, 1600)
pi.set_servo_pulsewidth(servo2, 1300)
pi.set_servo_pulsewidth(servo3, 1600)
time.sleep(2)

pi.set_servo_pulsewidth(servo1, 1600)
pi.set_servo_pulsewidth(servo2, 1500)
pi.set_servo_pulsewidth(servo3, 1400)
time.sleep(2)



pi.set_servo_pulsewidth(servo1, 1500)
pi.set_servo_pulsewidth(servo2, 1500)
pi.set_servo_pulsewidth(servo3, 1500)


pi.stop()