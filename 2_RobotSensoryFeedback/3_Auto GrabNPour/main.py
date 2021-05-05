from _XiaoRGEEK_SERVO_ import XR_Servo
from math import radians, sin, cos
from time import sleep, time
import RPi.GPIO as GPIO
import pygame
import sys

#############################################################################################
###            TASK 5: Max and Min Values of Robotic Arm + Grabbing & Pouring             ###
###                          Telerobotics, University of Birmingham                       ###
###                      Contributors: William Lubiantoro & Simon Chow                    ###
###                                   March 24, 2021                                      ###
#############################################################################################

# Global Values
Spd = 0.6
S1 = 55
S2 = 90
S3 = 170
S4 = 90

def basicConfig(s1, s2, s3, s4):
    """
    Moves robotic arm to its basic configuration from any arm configuration
    """
    global S1, S2, S3, S4

    if s1 > 55:
        for i in range (s1, 54, -1):
            Servo.XiaoRGEEK_SetServoAngle(1, i)
            S1 = i
    elif s1 < 55:
        for i in range (s1, 56, 1):
            Servo.XiaoRGEEK_SetServoAngle(1, i)
            S1 = i
    else:
        pass

    if s3 < 170:
        for i in range (s3, 171, 1):
            Servo.XiaoRGEEK_SetServoAngle(3, i)
            S3 = i
    elif s3 > 170:
        for i in range (s3, 169, -1):
            Servo.XiaoRGEEK_SetServoAngle(3, i)
            S3 = i
    else:
        pass

    if s2 > 90:
        for i in range (s2, 89, -1):
            Servo.XiaoRGEEK_SetServoAngle(2, i)
            S2 = i
    elif s2 < 90:
        for i in range (s2, 91, 1):
            Servo.XiaoRGEEK_SetServoAngle(2, i)
            S2 = i
    else:
        pass

    if s4 > 90:
        for i in range (s4, 89, -1):
            Servo.XiaoRGEEK_SetServoAngle(4, i)
            S4 = i
    elif s4 < 90:
        for i in range (s4, 91, 1):
            Servo.XiaoRGEEK_SetServoAngle(4, i)
            S4 = i
    else:
        pass

def grabConfig(s1, s2, s3, s4):
    """
    Moves robotic arm to its grabbing configuration from any arm configuration
    """
    global S1, S2, S3, S4
    if s3 < 125:
        for i in range (s3, 126, 1):
            Servo.XiaoRGEEK_SetServoAngle(3, i)
            S3 = i
    elif s3 > 125:
        for i in range (s3, 124, -1):
            Servo.XiaoRGEEK_SetServoAngle(3, i)
            S3 = i
    else:
        pass

    if s1 > 10:
        for i in range (s1, 9, -1):
            Servo.XiaoRGEEK_SetServoAngle(1, i)
            S1 = i
    elif s1 < 10:
        for i in range (s1, 11, 1):
            Servo.XiaoRGEEK_SetServoAngle(1, i)
            S1 = i
    else:
        pass

    if s2 > 90:
        for i in range(s2, 89, -1):
            Servo.XiaoRGEEK_SetServoAngle(2, i)
            S2 = i
    elif s2 < 90:
        for i in range(s2, 91, 1):
            Servo.XiaoRGEEK_SetServoAngle(2, i)
            S2 = i
    else:
        pass

    if s4 > 90:
        for i in range(s4, 89, -1):
            Servo.XiaoRGEEK_SetServoAngle(4, i)
            S4 = i
    elif s4 < 90:
        for i in range(s4, 91, 1):
            Servo.XiaoRGEEK_SetServoAngle(4, i)
            S4 = i
    else:
        pass

def get_distance():
    """
    Returns the distance read by the ultrasonic sensor in cm
    """
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

    dis = int((t2-t1)*340/2*100)
    if dis < 255:
        print(f"Distance: {dis} cm")
    return dis

def chk_vert_lim(s1, s2, s3):
    """
    Checks for the limit of the vertical component at 3 points of the robot arm (f, g, h).
    If any of these points go further than 10 degrees from Joint 1, angle won't change.

    Needs conversion robot angle to 0-degree at x-axis (through offset)
    S1    = 55 + tetha_1  (angle at Joint 1)
    S3_L  = 80 - tetha_2  (angle at Joint 2, short side of link 2)
    S3_h  = 154 - tetha_2 (angle at Joint 2, hypotenuse of link 2)
    """
    m = 9.7    # length of link 1
    nh = 14.56 # hypotenuse of the L link
    nc = 4     # short stick of the L link
    ef = -4.5  # End-effector radius
    if s2 != 90: # orientation of EF, other than 90 it effects vertical limit
        if s2 > 90:
            f = m * sin(radians(s1 - 55)) + nh * sin(radians(s1 - s3 + 99)) + ef * cos(radians(180-s2))
        elif s2 < 90:
            f = m * sin(radians(s1 - 55)) + nh * sin(radians(s1 - s3 + 99)) + ef * cos(radians(s2))
    else:
        f = m * sin(radians(s1 - 55)) + nh * sin(radians(s1 - s3 + 99))
    g = m * sin(radians(s1 - 55)) + nc * sin(radians(s1 - s3 + 25))
    y_total = min(f,g) # Gets smallest number between f & g
    #print(f" y total = {y_total}") # DEBUG
    return y_total

def grabNpour():
    """
    Function to automate the the process of grabbing and pouring a small bottle
    """
    #             S1  S2  S3   S4
    # initial  : (55, 90, 170, 90)
    # grab_pos : (10, 90, 125, 90)
    Servo.XiaoRGEEK_SetServoAngle(3, 125)
    sleep(1)
    Servo.XiaoRGEEK_SetServoAngle(1, 10)
    sleep(1)
    # grabbing : (10, 90, 125, 130)
    sleep(0.5)
    for S4 in range (90, 126, 1):
        Servo.XiaoRGEEK_SetServoAngle(4, S4)
    # lifting  : (55, 90, 170, 125)
    for S3 in range (125, 171, 1):
        Servo.XiaoRGEEK_SetServoAngle(1, S3 - 115)
        Servo.XiaoRGEEK_SetServoAngle(3, S3)
    # pouring  : (55, 0, 170, 125)
    for S2 in range (90, 181, 1):
        Servo.XiaoRGEEK_SetServoAngle(2, S2)
    sleep(1)
    # return   : (55, 90, 170, 125)
    for S2 in range(180, 89, -1):
        Servo.XiaoRGEEK_SetServoAngle(2, S2)
    # putting  : (10, 90, 125, 125)
    for S3 in range (170, 124, -1):
        Servo.XiaoRGEEK_SetServoAngle(3, S3)
        Servo.XiaoRGEEK_SetServoAngle(1, S3 - 115)
    # releasing: (10, 90, 125, 90)
    for S4 in range(125, 89, -1):
        Servo.XiaoRGEEK_SetServoAngle(4, S4)
    sleep(1)

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

def down(servo):
    """
    Function to decrease servo angles based on keyboard press
    """
    global S1, S2, S3, S4
    min_lim = - 10

    if servo == 1:
        S1 -= 5
        y_tot = chk_vert_lim(S1, S2, S3)
        if y_tot < min_lim:
            S1 += 5
            print(f"angle is {y_tot}! below -10 cm")
        else:
            if S1 <= 0:
                S1 = 0
            Servo.XiaoRGEEK_SetServoAngle(servo, S1)
    elif servo == 2:
        S2 -= 5
        y_tot = chk_vert_lim(S1, S2, S3)
        if y_tot < min_lim:
            S2 += 5
            print(f"angle is {y_tot}! below -10 cm")
        else:
            if S2 <= 0:
                S2 = 0
            Servo.XiaoRGEEK_SetServoAngle(servo, S2)
    elif servo == 3:
        S3 -= 5
        y_tot = chk_vert_lim(S1, S2, S3)
        if y_tot < min_lim:
            S3 += 5
            print(f"angle is {y_tot}! below -10 cm")
        else:
            if S3 <= 60:
                S3 = 60
            Servo.XiaoRGEEK_SetServoAngle(servo, S3)
    elif servo == 4:
        S4 -= 5
        if S4 <= 80:
            S4 = 80
        Servo.XiaoRGEEK_SetServoAngle(servo, S4)

def up(servo):
    """
    Function to increase servo angles based on keyboard press
    """
    global S1, S2, S3, S4
    min_lim = - 10

    if servo == 1:
        S1 += 5
        y_tot = chk_vert_lim(S1, S2, S3)
        if y_tot < min_lim:
            S1 -= 5
            print(f"angle is {y_tot}! below -10 cm")
        else:
            if S1 >= 180:
                S1 = 180
            Servo.XiaoRGEEK_SetServoAngle(servo, S1)
    elif servo == 2:
        S2 += 5
        y_tot = chk_vert_lim(S1, S2, S3)
        if y_tot < min_lim:
            S1 -= 5
            print(f"angle is {y_tot}! below -10 cm")
        else:
            if S2 >= 180:
                S2 = 180
            Servo.XiaoRGEEK_SetServoAngle(servo, S2)
    elif servo == 3:
        S3 += 5
        y_tot = chk_vert_lim(S1, S2, S3)
        if y_tot < min_lim:
            S3 -= 5
            print(f"angle is {y_tot}! below -10 cm")
        else:
            if S3 >= 180:
                S3 = 180
            Servo.XiaoRGEEK_SetServoAngle(servo, S3)
    elif servo == 4:
        S4 += 5
        if S4 >= 140:
            S4 = 140
        Servo.XiaoRGEEK_SetServoAngle(servo, S4)

def move(L_Spd = 0.6, R_Spd = 0.6):
    """
    Function for 360 robot movement based on keyboard presses
    """
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
    """
    main function in while loop
    """
    global Spd, S1, S2, S3, S4

    dis = get_distance() # Gets and prints distance from ultrasonic sensor

    # Robot Movements
    if dis > 30: # move any direction while distance above 30 cm
        if getKey('w'):
            if getKey('a'):
                move(Spd - 0.25, Spd)
            elif getKey('d'):
                move(Spd, Spd - 0.25)
            else:
                move(Spd, Spd)
        elif getKey('s'):
            if getKey('a'):
                move(-Spd + 0.25, -Spd)
            elif getKey('d'):
                move(-Spd, -Spd + 0.25)
            else:
                move(-Spd, -Spd)
        elif getKey('d'):
            move(Spd, -Spd)
        elif getKey('a'):
            move(-Spd, Spd)

        else: move(0, 0)
    else: # cannot move forward for a distance smaller than 30 cm
        if getKey('s'):
            if getKey('a'):
                move(-Spd + 0.25, -Spd)
            elif getKey('d'):
                move(-Spd, -Spd + 0.25)
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

    # Servo Control
    if getKey('KP4'):
        down(1)
    elif getKey('KP7'):
        up(1)
    elif getKey('KP9'):
        down(2)
    elif getKey('KP6'):
        up(2)
    elif getKey('KP1'):
        down(3)
    elif getKey('KP3'):
        up(3)
    elif getKey('KP_MINUS'):
        down(4)
    elif getKey('KP_PLUS'):
        up(4)

    # Shortcuts to pre-determined configs
    elif getKey('g'):
        grabConfig(S1,S2,S3,S4)

    elif getKey('b'):
        basicConfig(S1,S2,S3,S4)
    
    elif getKey('p'):
        grabNpour()

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