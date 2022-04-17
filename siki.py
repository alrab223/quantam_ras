import math
class Angle:
    def __init__(self):
        self.servo1 = 2#緑ケーブル
        self.servo2 = 12#前転に難あり、紫ケーブル
        self.servo3=26
        self.servo1_pwm = 1500
        self.servo2_pwm = 1500
        self.servo3_pwm = 1500
        self.servo1_angle = 90
        self.servo2_angle = 210
        self.servo3_angle = 330
        self.speed=100

    def angle_control(self, angle):
        coefficient1 = round(math.cos(math.radians(angle - self.servo1_angle))*(-1),6)
        coefficient2 = round(math.cos(math.radians(angle - self.servo2_angle))*(-1),6)
        coefficient3 = round(math.cos(math.radians(angle - self.servo3_angle))*(-1),6)
        print(coefficient1, coefficient2, coefficient3)
        return coefficient1,coefficient2,coefficient3
    
    def main(self):
        angle = self.angle_control(90)
        print(angle)
        angle = [x * self.speed for x in angle]
        print(angle)

Angle().main()
      