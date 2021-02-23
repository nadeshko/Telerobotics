import os, sys
from KeyPress_Module import KeyPress
#from RobotControl import Robot_Control

import RPi.GPIO as GPIO
from _XiaoRGEEK_SERVO_ import XR_Servo
from time import sleep

# Setup pygame
Kp = KeyPress()
# https://www.pygame.org/docs/ref/key.html

## Set GPIO call mode as BCM
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Initializing Servo for robot arms
Servo = XR_Servo()

## Define Ports
ENA = 13
ENB = 20
IN1 = 19
IN2 = 16
IN3 = 21
IN4 = 26

# Initial Values
Speed = 75
S1_Angle = 10
S2_Angle = 120
S3_Angle = 90
S4_Angle = 0
S7_Angle = 0
S8_Angle = 90
img_counter = 0
Servo.XiaoRGEEK_SetServoAngle(1, S1_Angle)
Servo.XiaoRGEEK_SetServoAngle(2, S2_Angle)
Servo.XiaoRGEEK_SetServoAngle(3, S3_Angle)
Servo.XiaoRGEEK_SetServoAngle(4, S4_Angle)
Servo.XiaoRGEEK_SetServoAngle(7, S7_Angle)
Servo.XiaoRGEEK_SetServoAngle(8, S8_Angle)

# Port Setup
print("Start")
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

# Specify the PWM control port and the frequency of the PWM signal
RightM = GPIO.PWM(ENA, 1000)
LeftM = GPIO.PWM(ENB, 1000)

# Start PWM
RightM.start(75)
LeftM.start(75)

# Define movement functions
def Forward():
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def ForLeft():
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    RightM.ChangeDutyCycle(100)
    LeftM.ChangeDutyCycle(45)

def ForRight():
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    RightM.ChangeDutyCycle(45)
    LeftM.ChangeDutyCycle(100)

def Backward():
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def Left():
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def Right():
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

## Define a function to stop
def Stop():
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

def main():
    global S1_Angle
    global S2_Angle
    global S3_Angle
    global S4_Angle
    global S7_Angle
    global S8_Angle
    window = True

    if Kp.getKey('w'):
        if Kp.getKey('d'):
            ForRight()
            #Robot_Control('wd')
        elif Kp.getKey('a'):
            ForLeft()
            #Robot_Control('wa')
        else: Forward() #Robot_Control('w')
    elif Kp.getKey('s'):
        '''if Kp.getKey('d'):
            Robot_Control('sd')
        elif Kp.getKey('a'):
            Robot_Control('sa')
        else: Robot_Control('s')'''
        Backward()
    elif Kp.getKey('a'):
        Right()
        #Robot_Control('a')
    elif Kp.getKey('d'):
        Left()
        #Robot_Control('d')
    #elif Kp.getKey('LSHIFT'):
        #Robot_Control('LSHIFT')
    elif Kp.getKey('q'):
        print('quitting')
        window = False

    # Servo 1 Control
    elif Kp.getKey('KP4'):
        if S1_Angle <= 0:
            S1_Angle = 0
        else:
            S1_Angle -= 5
        Servo.XiaoRGEEK_SetServoAngle(1, S1_Angle)
    elif Kp.getKey('KP7'):
        if S1_Angle >= 180:
            S1_Angle = 180
        else:
            S1_Angle += 5
        Servo.XiaoRGEEK_SetServoAngle(1, S1_Angle)
    # Servo 2 Control
    elif Kp.getKey('KP9'):
        if S2_Angle <= 0:
            S2_Angle = 0
        else:
            S2_Angle -= 5
        Servo.XiaoRGEEK_SetServoAngle(2, S2_Angle)
    elif Kp.getKey('KP6'):
        if S2_Angle >= 180:
            S2_Angle = 180
        else:
            S2_Angle += 5
        Servo.XiaoRGEEK_SetServoAngle(2, S2_Angle)
    # Servo 3 Control
    elif Kp.getKey('KP3'):
        if S3_Angle >= 180:
            S3_Angle = 180
        else:
            S3_Angle += 5
        Servo.XiaoRGEEK_SetServoAngle(3, S3_Angle)
    elif Kp.getKey('KP1'):
        if S3_Angle <= 0:
            S3_Angle = 0
        else:
            S3_Angle -= 5
        Servo.XiaoRGEEK_SetServoAngle(3, S3_Angle)
    # Servo 4 Control
    elif Kp.getKey('KP_MINUS'):
        if S4_Angle <= 0:
            S4_Angle = 0
        else:
            S4_Angle -= 5
        Servo.XiaoRGEEK_SetServoAngle(4, S4_Angle)9*
    elif Kp.getKey('KP_PLUS'):
        if S4_Angle >= 90:
            S4_Angle = 90
        else:
            S4_Angle += 5
        Servo.XiaoRGEEK_SetServoAngle(4, S4_Angle)

    # Servo 7 and 8
    elif Kp.getKey('UP'):
        if S7_Angle <= 0:
            S7_Angle = 0
        else:
            S7_Angle -= 5
        Servo.XiaoRGEEK_SetServoAngle(7, S7_Angle)
    elif Kp.getKey('DOWN'):
        if S7_Angle >= 90:
            S7_Angle = 90
        else:
            S7_Angle += 5
        Servo.XiaoRGEEK_SetServoAngle(7, S7_Angle)
    elif Kp.getKey('LEFT'):
        if S8_Angle <= 0:
            S8_Angle = 0
        else:
            S8_Angle -= 5
        Servo.XiaoRGEEK_SetServoAngle(8, S8_Angle)
    elif Kp.getKey('RIGHT'):
        if S8_Angle >= 90:
            S8_Angle = 90
        else:
            S8_Angle += 5
        Servo.XiaoRGEEK_SetServoAngle(8, S8_Angle)

    else:
        Stop()
        #Robot_Control('STOP')
    return window

if __name__ == '__main__':
    while True:
        window = main()
        if window == False:
            break