from _XiaoRGEEK_SERVO_ import XR_Servo
from time import sleep, time
import RPi.GPIO as GPIO
import pygame
import sys

Spd = 0.6

def get_distance():
    sleep(0.0005)
    GPIO.output(TRIG, GPIO.HIGH)
    sleep(0.000015)
    GPIO.output(TRIG, GPIO.LOW)
    while not GPIO.input(ECHO):
        pass
    t1 = time()
    while GPIO.input(ECHO):
        pass
    t2 = time()
    #sleep(0.1)

    dis = int((t2-t1)*340/2*100)
    if dis < 255:
        print(f"Distance: {dis} cm")
    return dis

def basicConfig():
    Servo.XiaoRGEEK_SetServoAngle(1, 55)
    Servo.XiaoRGEEK_SetServoAngle(2, 90)
    Servo.XiaoRGEEK_SetServoAngle(3, 170)
    Servo.XiaoRGEEK_SetServoAngle(4, 90)

def grabNpour():
    #             S1  S2  S3   S4
    # initial  : (55, 90, 170, 90)
    # grab_pos : (10, 90, 125, 90)
    Servo.XiaoRGEEK_SetServoAngle(3, 125)
    sleep(1)
    Servo.XiaoRGEEK_SetServoAngle(1, 10)
    sleep(1)
    # grabbing : (10, 90, 125, 125)
    for S4 in range (90, 125, 5):
        Servo.XiaoRGEEK_SetServoAngle(4, S4)
        sleep(0.75)
    sleep(1)
    # lifting  : (55, 90, 170, 125)
    for S3 in range (125, 175, 5):
        Servo.XiaoRGEEK_SetServoAngle(3, S3)
        sleep(0.75)
        Servo.XiaoRGEEK_SetServoAngle(1, S3-115)
        sleep(0.75)
    sleep(1)
    # pouring  : (55, 0, 170, 125)
    for S2 in range (90, -5, -10):
        Servo.XiaoRGEEK_SetServoAngle(2, S2)
        sleep(0.75)
    sleep(1)
    # return   : (55, 90, 170, 125)
    Servo.XiaoRGEEK_SetServoAngle(2, 90)
    sleep(1)
    # putting  : (10, 90, 125, 90)
    Servo.XiaoRGEEK_SetServoAngle(3, 125)
    sleep(1)
    Servo.XiaoRGEEK_SetServoAngle(1, 10)
    sleep(1)
    Servo.XiaoRGEEK_SetServoAngle(4, 90)
    sleep(3)

def getKey(key):
    """
    Detects keyboard input, returns True if keyboard is pressed
    """
    Pressed = False
    for event in pygame.event.get(): pass
    keyPress = pygame.key.get_pressed()
    keyName = getattr(pygame, 'K_{}'.format(key))
    if keyPress[keyName]:
        Pressed = True
    pygame.display.update()
    return Pressed

def move(L_Spd = 0.6, R_Spd = 0.6):
    R_Spd *= 100
    L_Spd *= 100

    if R_Spd > 0:
        RightM.ChangeDutyCycle(R_Spd)
        GPIO.output(ENA, True)
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)
    elif R_Spd == 0:
        RightM.ChangeDutyCycle(0)
        GPIO.output(ENA, False)
        GPIO.output(IN1, False)
        GPIO.output(IN2, False)
    else:
        RightM.ChangeDutyCycle(-R_Spd)
        GPIO.output(ENA, True)
        GPIO.output(IN1, True)
        GPIO.output(IN2, False)

    if L_Spd > 0:
        LeftM.ChangeDutyCycle(L_Spd)
        GPIO.output(ENB, True)
        GPIO.output(IN3, False)
        GPIO.output(IN4, True)
    elif L_Spd == 0:
        LeftM.ChangeDutyCycle(0)
        GPIO.output(ENB, False)
        GPIO.output(IN3, False)
        GPIO.output(IN4, False)
    else:
        LeftM.ChangeDutyCycle(-L_Spd)
        GPIO.output(ENB, True)
        GPIO.output(IN3, True)
        GPIO.output(IN4, False)

def main():
    global Spd

    dis = get_distance()

    # Robot Movements
    if dis > 34:
        if getKey('w'):
            if getKey('a'):
                move(0.5, 0.85)
            elif getKey('d'):
                move(0.85, 0.5)
            else:
                move(Spd, Spd)
        elif getKey('s'):
            if getKey('a'):
                move(-0.5, -0.85)
            elif getKey('d'):
                move(-0.85, -0.5)
            else:
                move(-Spd, -Spd)
        elif getKey('d'):
            move(Spd, -Spd)
        elif getKey('a'):
            move(-Spd, Spd)

        else: move(0, 0)
    else:
        if getKey('s'):
            if getKey('a'):
                move(-0.5, -0.85)
            elif getKey('d'):
                move(-0.85, -0.5)
            else:
                move(-Spd, -Spd)
        elif getKey('d'):
            move(Spd, -Spd)
        elif getKey('a'):
            move(-Spd, Spd)
        else: move(0, 0)

    # Robot acceleration/deceleration
    if getKey('LSHIFT'):
        if Spd >= 1:
            Spd = 1
        else:
            Spd += 0.1
            print(f"Speed = {Spd}")
    elif getKey('LCTRL'):
        if Spd <= 0.4:
            Spd = 0.4
        else:
            Spd -= 0.1
            print(f"Speed = {Spd}")

    elif getKey('KP_1'):
        #TODO: vertical angle limits
        pass

    elif getKey('g'):
        grabNpour()
        basicConfig()

if __name__ == '__main__':
    # Initialize pygame and opens window
    pygame.init()
    screen = pygame.display.set_mode((200, 200))

    # Set GPIO call mode as BCM
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Initializing Servo for robot arms
    Servo = XR_Servo()

    ## Define Ports
    ENA = 13
    ENB = 20
    IN1 = 19
    IN2 = 16
    IN3 = 21
    IN4 = 26
    ECHO = 4
    TRIG = 17

    # Initial values
    S1 = 55  # 10
    S2 = 90
    S3 = 170  # 125
    S4 = 90
    Servo.XiaoRGEEK_SetServoAngle(1, S1)
    Servo.XiaoRGEEK_SetServoAngle(2, S2)
    Servo.XiaoRGEEK_SetServoAngle(3, S3)
    Servo.XiaoRGEEK_SetServoAngle(4, S4)

    # Port Setup
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ECHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Specify the PWM control port and the frequency of the PWM signal
    RightM = GPIO.PWM(ENA, 1000)
    LeftM = GPIO.PWM(ENB, 1000)

    # Start PWM
    RightM.start(0)
    LeftM.start(0)

    try:
        while True:
            main()

    except KeyboardInterrupt:
        pygame.display.quit()
        pygame.quit()
        sys.exit()