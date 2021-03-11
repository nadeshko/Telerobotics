from socket import *
from time import ctime
import binascii
import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ECHO = 4
TRIG = 17

GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def Get_Distance():
 time.sleep(0.05)
 GPIO.output(TRIG,GPIO.HIGH)
 time.sleep(0.000015)
 GPIO.output(TRIG,GPIO.LOW)
 while not GPIO.input(ECHO):
  pass
 t1 = time.time()
 while GPIO.input(ECHO):
  pass
 t2 = time.time()
 time.sleep(0.1)
 return (t2-t1)*340/2*100
 
def Send_Distance():
 dis_send = int(Get_Distance())
 #dis_sned = str("%.2f"dis_send)
 if dis_send<255:
  print('Distane: %d cm',dis_send)
  
while True:
 Send_Distance()