import time
import RPi.GPIO as GPIO
from _XiaoRGEEK_SERVO_ import XR_Servo
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Servo = XR_Servo()

## Set servo 1 angle as 135 degree
Servo.XiaoRGEEK_SetServoAngle(2,179)
time.sleep(1)

## Save all servo angles at this point
Servo.XiaoRGEEK_SaveServo()
time.sleep(1)

## Set Servo 1 angle as 150 degree
## Servo.XiaoRGEEK_SetServoAngle(1,90)
## time.sleep(1)

## Restore all servo servo angls to their saved default values
Servo.XiaoRGEEK_ReSetServo()
