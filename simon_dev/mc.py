# Motor Control With command

import time
import RPi.GPIO as GPIO

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

## Initialize
print("Start")
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

## Define a function to move forward
def Forward():
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,False)
 GPIO.output(IN2,True)
 GPIO.output(IN3,False)
 GPIO.output(IN4,True)

## Define a function to move backward
def Backward():
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,True)
 GPIO.output(IN2,False)
 GPIO.output(IN3,True)
 GPIO.output(IN4,False)

## Define a function to turn left
def Left():
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,False)
 GPIO.output(IN2,False)
 GPIO.output(IN3,False)
 GPIO.output(IN4,False)

## Define a function to turn right
def Right():
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,False)
 GPIO.output(IN2,False)
 GPIO.output(IN3,False)
 GPIO.output(IN4,False)

 ## Define a function to stop
def Stop():
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,False)
 GPIO.output(IN2,False)
 GPIO.output(IN3,False)
 GPIO.output(IN4,False)
 
while True:
 var=input()
 if (var=="w"):
  Forward(1)
  Stop()
 elif (var=="s"):
  Backward(1)
  Stop()
 elif (var=="a"):
  left(1)
  Stop()
 elif (var=="d"):
  right(1)
  Stop()