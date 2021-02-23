import time
import RPi.GPIO as GPIO
from _XiaoRGEEK_SERVO_ import XR_Servo
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Servo = XR_Servo()