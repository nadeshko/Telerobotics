# Motor Control With command

import time
import RPi.GPIO as GPIO
from time import sleep

## Set GPIO call mode as BCM
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

## Defined Ports
ENA=13
ENB=20
IN1=19
IN2=16
IN3=21
IN4=26
Speed = 0

## Initialize
print("Start")
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

# Specify the PWM control port and the frequency of the PWM signal
PWM1=GPIO.PWM(ENA,1000)
PWM2=GPIO.PWM(ENB,1000)

# Start PWMPWM.start(0)
PWM1.start(0)
PWM2.start(0)

## Define a function to move forward
def Forward(x):
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,False)
 GPIO.output(IN2,True)
 GPIO.output(IN3,False)
 GPIO.output(IN4,True)
 sleep(x)

## Define a function to move backward
def Backward(x):
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,True)
 GPIO.output(IN2,False)
 GPIO.output(IN3,True)
 GPIO.output(IN4,False)
 sleep(x)

 ## Define a function to stop
def Stop():
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,False)
 GPIO.output(IN2,False)
 GPIO.output(IN3,False)
 GPIO.output(IN4,False)
 
def Hundred():
    PWM1.ChangeDutyCycle(100)
    PWM2.ChangeDutyCycle(100)
    
def Fifty():
    PWM1.ChangeDutyCycle(50)
    PWM2.ChangeDutyCycle(50)
 
 
while True:
 var=input()
 if (var=="w"):
  Forward(1)
  Stop()
 elif (var=="s"):
  Backward(1)
  Stop()
 elif (var=="i"):
  Hundred()
 elif (var=="j"):
  Fifty()