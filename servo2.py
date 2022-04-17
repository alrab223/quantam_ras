import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

ch = 1

def fs90r_convert(throttle):
    """
    Parameters
    ----------
    throttle : float
      require -1.0 .. 1.0, but no check

    Returns : float
      -0.4(right rotation) <= 0.1(stop) <= 0.6(left rotation)
    """
    return 0.1 + throttle / 2

# left rotation (0.1 .. 1.0(max))
for i in range(1,11):
    v = fs90r_convert(i/10)
    print( "i=%f v=%f" % (i/10, v) )
    kit.continuous_servo[ch].throttle = v
    time.sleep(1)

# right rotation (-0.1 .. -1.0(max))
for i in range(-1,-11,-1):
    v = fs90r_convert(i/10)
    print( "i=%f v=%f" % (i/10, v) )
    kit.continuous_servo[ch].throttle = v
    time.sleep(1)

# stop rotation
kit.continuous_servo[ch].throttle = fs90r_convert(0)
time.sleep(1)

# left rotation, max throttle
kit.continuous_servo[ch].throttle = fs90r_convert(1)
time.sleep(1)

# right rotation, half throttle
kit.continuous_servo[ch].throttle = fs90r_convert(-0.5)
time.sleep(1)

# stop rotation
kit.continuous_servo[ch].throttle = fs90r_convert(0)