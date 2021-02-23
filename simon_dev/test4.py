import time
import RPi.GPIO as GPIO
import binascii #??
from smbus import SMBus  #??
XRservo=SMBus(1)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

time.sleep(2)
XRservo.XiaoRGEEK_SetServo(0x01,90)
print('ser1=90')
time.sleep(0.5)
XRservo.XiaoRGEEK_SetServo(0x01,30)
print('ser1=30 -> save')
time.sleep(0.1)
XRservo.XiaoRGEEK_SetServo()
time.sleep(0.5)
XRservo.XiaoRGEEK_SetServo(0x01,90)
print('ser1=90')
time.sleep(0.5)
XRservo.XiaoRGEEK_SetServo(0x01,150)
print('ser1=150')
time.sleep(1.5)
XRservo.XiaoRGEEK_SetServo()
print('back to 30 as saved')