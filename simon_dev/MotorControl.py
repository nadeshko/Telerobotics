import RPi.GPIO as GPIO
import time

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
Speed=5




# Stop PWM
# PWM.stop()

## Initialize
print("Start")
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
# Specify the PWM control port and the frequency of the PWM signal
PWM=GPIO.PWM(ENA,1000)

# Start PWMPWM.start(0)



## Define a function to move forward
def MoveForward():
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,False)
 GPIO.output(IN2,False)
 GPIO.output(IN4,True)
 GPIO.output(IN3,False)
 
## Define a function to stop
def Stop():
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,False)
 GPIO.output(IN2,False)
 GPIO.output(IN3,False)
 GPIO.output(IN4,False)
 
## Main Loop
if __name__=="__main__":
 PWM.start(0)
 print("Yes")
 MoveForward()
 time.sleep(1)
 PWM.ChangeDutyCycle(Speed)
 Stop()
 time.sleep(1)