import RPi.GPIO as GPIO
import pygame
import cv2
from _XiaoRGEEK_SERVO_ import XR_Servo

#Initialize pygame and opens window
pygame.init()
screen = pygame.display.set_mode([500,300])

# Set GPIO call mode as BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Initializing Servo for robot arms
Servo = XR_Servo()

# Allow Camera
#cam = cv2.VideoCapture(0)

## Define Ports
ENA=13
ENB=20
IN1=19
IN2=16
IN3=21
IN4=26

# Initial Values
x = 0
y = 0
Speed = 0
rotate = 0
S1 = 10
S2 = 90
S3 = 125
S4 = 90
S7 = 0
S8 = 80
#img_counter = 0
edit_img_clear = True
Servo.XiaoRGEEK_SetServoAngle(1,S1)
Servo.XiaoRGEEK_SetServoAngle(2,S2)
Servo.XiaoRGEEK_SetServoAngle(3,S3)
Servo.XiaoRGEEK_SetServoAngle(4,S4)
Servo.XiaoRGEEK_SetServoAngle(7,S7)
Servo.XiaoRGEEK_SetServoAngle(8,S8)

# Port Setup
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

# Specify the PWM control port and the frequency of the PWM signal
RightM=GPIO.PWM(ENA,1000)
LeftM=GPIO.PWM(ENB,1000)

# Start PWM
RightM.start(0)
LeftM.start(0)

# Define robot movement functions
def Forward(Spd):
    Spd *= 100
    RightM.ChangeDutyCycle(Spd)
    LeftM.ChangeDutyCycle(Spd)
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
def Backward(Spd):
    Spd *= 100
    RightM.ChangeDutyCycle(Spd)
    LeftM.ChangeDutyCycle(Spd)
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
def Right(Spd):
    Spd *= 100
    RightM.ChangeDutyCycle(Spd)
    LeftM.ChangeDutyCycle(Spd)
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
def Left(Spd):
    Spd *= 100
    RightM.ChangeDutyCycle(Spd)
    LeftM.ChangeDutyCycle(Spd)
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
def Stop():
    RightM.ChangeDutyCycle(0)
    LeftM.ChangeDutyCycle(0)
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

# Define servo movements
def down(servo):
    global S1, S2, S3, S4, S7, S8
    if servo == 1:
        S1 -= 5
        if S1 <= 0:
            S1 = 0
        Servo.XiaoRGEEK_SetServoAngle(servo, S1)
    elif servo == 2:
        S2 -= 5
        if S2 <= 0:
            S2 = 0
        Servo.XiaoRGEEK_SetServoAngle(servo, S2)
    elif servo == 3:
        S3 -= 5
        if S3 <= 0:
            S3 = 0
        Servo.XiaoRGEEK_SetServoAngle(servo, S3)
    elif servo == 4:
        S4 -= 5
        if S4 <= 80:
            S4 = 80
        Servo.XiaoRGEEK_SetServoAngle(servo, S4)
    elif servo == 7:
        S7 -= 5
        if S7 <= 0:
            S7 = 0
        Servo.XiaoRGEEK_SetServoAngle(servo, S7)
    elif servo == 8:
        S8 -= 5
        if S8 <= 0:
            S8 = 0
        Servo.XiaoRGEEK_SetServoAngle(servo, S8)
def up(servo):
    global S1, S2, S3, S4, S7, S8
    if servo == 1:
        S1 += 5
        if S1 >= 180:
            S1 = 180
        Servo.XiaoRGEEK_SetServoAngle(servo, S1)
    elif servo == 2:
        S2 += 5
        if S2 >= 180:
            S2 = 180
        Servo.XiaoRGEEK_SetServoAngle(servo, S2)
    elif servo == 3:
        S3 += 5
        if S3 >= 180:
            S3 = 180
        Servo.XiaoRGEEK_SetServoAngle(servo, S3)
    elif servo == 4:
        S4 += 5
        if S4 >= 140:
            S4 = 140
        Servo.XiaoRGEEK_SetServoAngle(servo, S4)
    elif servo == 7:
        S7 += 5
        if S7 >= 90:
            S7 = 90
        Servo.XiaoRGEEK_SetServoAngle(servo, S7)
    elif servo == 8:
        S8 += 5
        if S8 >= 180:
            S8 = 180
        Servo.XiaoRGEEK_SetServoAngle(servo, S8)

if __name__ == '__main__':
    while True:

        #ret, frame = cam.read()
        #cv2.imshow('Camera', frame)
        '''
        k = cv2.waitKey(1) % 256
        if k == 27:  # ESC
            print("quitting...")
            break
        elif k == 32:  # Space
            if edit_img_clear == True:
                print('\nPress g to make an image grayscale!')
                print('Press s resize an image!')
                print('Press r rotate an image!')
                print('Press q to close windows!\n')
                edit_img_clear = False
            img_name = "frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
        elif k == ord('q'):
            cv2.destroyAllWindows()
        elif k == ord('g'):  # Grayscale
            img = input("In integer, which picture would you like to make grayscale?")
            gray_img = cv2.imread(f"frame_{img}.png", 0)
            if gray_img is not None:
                print(f"Changing frame_{img}.png to grayscale!")
                cv2.imshow("Grayscale Image", gray_img)
                cv2.waitKey(0)
                cv2.destroyWindow("Grayscale Image")
            else:
                print('image couldnt be read! try again')
        elif k == ord('s'):  # Resize
            img = input("In integer, which picture would you like to resize?")
            to_resize = cv2.imread(f"frame_{img}.png")
            if to_resize is not None:
                y = int(input("How tall?"))
                x = int(input("How long horizontally?"))
                print(f"resizing frame_{img}.png to [{x},{y}]")
                resized_img = cv2.resize(to_resize, (x, y))
                cv2.imshow("Resized Image", resized_img)
                cv2.waitKey(0)
                cv2.destroyWindow("Resized Image")
            else:
                print('image couldnt be read! try again')
        elif k == ord('r'):  # Rotate
            img = input("In integer, which picture would you like to rotate?")
            to_rotate = cv2.imread(f"frame_{img}.png")
            if to_rotate is not None:
                rotate = input("Turning clockwise, how much degree do you want it to turn? (90, 180, 270)")
                rotation = getattr(cv2, f"ROTATE_{rotate}_CLOCKWISE")
                rotated_img = cv2.rotate(to_rotate, rotation)
                cv2.imshow("Rotated Image", rotated_img)
                cv2.waitKey(0)
                cv2.destroyWindow("Rotated Image")
            else:
                print('image couldnt be read! try again')
        '''
        # Keyboard inputs
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Robot Movements
                if event.key == pygame.K_w:
                    Forward(Speed)
                    print('Moving Forward')
                elif event.key == pygame.K_s:
                    Backward(Speed)
                    print('Moving backwards')
                elif event.key == pygame.K_a:
                    Left(Speed)
                    print('Turning left')
                elif event.key == pygame.K_d:
                    Right(Speed)
                    print('Turning right')

                # Robot acceleration/decceleration
                elif event.key == pygame.K_LSHIFT:
                    if Speed >= 1:
                        Speed = 1
                    else:
                        Speed += 0.1
                        print(Speed)
                elif event.key == pygame.K_LCTRL:
                    if Speed <= 0:
                        Speed = 0
                    else:
                        Speed -= 0.1
                        print(Speed)

                # Servo 1 Control
                elif event.key == pygame.K_KP4:
                    down(1)
                elif event.key == pygame.K_KP7:
                    up(1)
                # Servo 2 Control
                elif event.key == pygame.K_KP9:
                    down(2)
                elif event.key == pygame.K_KP6:
                    up(2)
                # Servo 3 Control
                elif event.key == pygame.K_KP1:
                    down(3)
                elif event.key == pygame.K_KP3:
                    up(3)
                # Servo 4 Control
                elif event.key == pygame.K_KP_MINUS:
                    down(4)
                elif event.key == pygame.K_KP_PLUS:
                    up(4)
                # Servo 7 Control
                elif event.key == pygame.K_UP:
                    down(7)
                elif event.key == pygame.K_DOWN:
                    up(7)
                # Servo 8 Control
                elif event.key == pygame.K_RIGHT:
                    down(8)
                elif event.key == pygame.K_LEFT:
                    up(8)

                elif event.key == pygame.K_ESCAPE:
                    print("quitting...")
                    break
            elif event.type == pygame.KEYUP:
                Stop()

#cam.release()
#cv2.destroyAllWindows()