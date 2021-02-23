import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LED0=10
LED1=9
LED2=25
GPIO.setwarnings(False)
GPIO.setup(LED0,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(LED1,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(LED2,GPIO.OUT,initial=GPIO.HIGH)
def init_light():
 GPIO.output(LED0,False)
 GPIO.output(LED1,False)
 GPIO.output(LED2,False)
 time.sleep(0.5)
 GPIO.output(LED0,True)
 GPIO.output(LED1,False)
 GPIO.output(LED2,False)
 time.sleep(0.5)
 GPIO.output(LED0,False)
 GPIO.output(LED1,True)
 GPIO.output(LED2,False)
 time.sleep(0.5)
 GPIO.output(LED0,False)
 GPIO.output(LED1,False)
 GPIO.output(LED2,True)
 time.sleep(0.5)
 GPIO.output(LED0,False)
 GPIO.output(LED1,False)
 GPIO.output(LED2,False)
 time.sleep(0.5)
 GPIO.output(LED0,True)
 GPIO.output(LED1,True)
 GPIO.output(LED2,True)
 time.sleep(0.5)
for i in range(1,5):
 init_light()