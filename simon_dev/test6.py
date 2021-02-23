import time
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
LED0=10
LED1=9
LED2=25
GPIO.setwarnings(False)
GPIO.setup(LED0,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED2,GPIO.OUT,initial=GPIO.LOW)

def forward(s):
 print('Going Farwards')
 GPIO.output(LED0,GPIO.HIGH)
 GPIO.output(LED1,GPIO.HIGH)
 GPIO.output(LED2,GPIO.HIGH)
 sleep(s)
 
def backward(s):
 print('Going Backwards')
 GPIO.output(LED0,GPIO.LOW)
 GPIO.output(LED1,GPIO.LOW)
 GPIO.output(LED2,GPIO.LOW)
 sleep(s)
 
def left(s):
 print('Going Left')
 GPIO.output(LED0,GPIO.HIGH)
 GPIO.output(LED1,GPIO.LOW)
 GPIO.output(LED2,GPIO.HIGH)
 sleep(s)
 
def right(s):
 print('Going Right')
 GPIO.output(LED0,GPIO.LOW)
 GPIO.output(LED1,GPIO.HIGH)
 GPIO.output(LED2,GPIO.LOW)
 sleep(s)
 

while True:
 var=input()
 if (var=="w"):
  forward(1)
  #Stop()
 elif (var=="s"):
  backward(1)
  #Stop()
 elif (var=="a"):
  left(1)
  #Stop()
 elif (var=="d"):
  right(1)
  #Stop()

# GPIO.cleanup()

# def init_light():
#  while true)
# char = raw_input()
# if (char=="a")
## GPIO.output(LED0,False)
# GPIO.output(LED1,False)
# GPIO.output(LED2,False)
# # time.sleep(0.5)
# if (char=="b")
# GPIO.output(LED0,True)
# GPIO.output(LED1,False)
# GPIO.output(LED2,False)
# # time.sleep(0.5)
# if (char=="c")
# GPIO.output(LED0,False)
# GPIO.output(LED1,True)
# GPIO.output(LED2,False)
# # time.sleep(0.5)
# if (char=="d")
# GPIO.output(LED0,False)
# GPIO.output(LED1,False)
# GPIO.output(LED2,True)
 # time.sleep(0.5)
 # GPIO.output(LED0,False)
 # GPIO.output(LED1,False)
 # GPIO.output(LED2,False)
 # time.sleep(0.5)
# if (char=="e")
# GPIO.output(LED0,True)
# GPIO.output(LED1,True)
# GPIO.output(LED2,True)
# time.sleep(0.5)
# if (char=="f")
# break
#for i in range(1,5):
# init_light()