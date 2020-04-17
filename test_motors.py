"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1 cuz idk what type these are"""
import time
from adafruit_servokit import ServoKit
 
# Set channels to the number available
kit = ServoKit(channels=16)
 
kit.servo[0].angle = 180
kit.continuous_servo[1].throttle = 1
time.sleep(1)
kit.continuous_servo[1].throttle = -1
time.sleep(1)
kit.servo[0].angle = 0
kit.continuous_servo[1].throttle = 0
