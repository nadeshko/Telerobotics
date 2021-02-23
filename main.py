import RPi.GPIO as GPIO
from time import sleep
import pygame, os, time
import cv2
from _XiaoRGEEK_SERVO_ import XR_Servo

screen = pygame.display.set_mode([500,300])

## Set GPIO call mode as BCM
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Allow Camera
cam = cv2.VideoCapture(0)

# Initializing Servo for robot arms
Servo = XR_Servo()

## Define Ports
ENA=13
ENB=20
IN1=19
IN2=16
IN3=21
IN4=26

# Initial Values
Speed = 0
S1_Angle = 10
S2_Angle = 120
S3_Angle = 90
S4_Angle = 0
img_counter = 0
Servo.XiaoRGEEK_SetServoAngle(1,S1_Angle)
Servo.XiaoRGEEK_SetServoAngle(2,S2_Angle)
Servo.XiaoRGEEK_SetServoAngle(3,S3_Angle)
Servo.XiaoRGEEK_SetServoAngle(4,S4_Angle)

# Port Setup
print("Start")
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
 
## Define a function to turn right
def Right():
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,True)
 GPIO.output(IN2,False)
 GPIO.output(IN3,False)
 GPIO.output(IN4,True)

## Define a function to turn left
def Left():
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,False)
 GPIO.output(IN2,True)
 GPIO.output(IN3,True)
 GPIO.output(IN4,False)

 ## Define a function to stop
def Stop():
 GPIO.output(ENA,True)
 GPIO.output(ENB,True)
 GPIO.output(IN1,False)
 GPIO.output(IN2,False)
 GPIO.output(IN3,False)
 GPIO.output(IN4,False)
 
def spd_Eco():
    RightM.ChangeDutyCycle(50)
    LeftM.ChangeDutyCycle(50)
    
def spd_Comfort():
    RightM.ChangeDutyCycle(75)
    LeftM.ChangeDutyCycle(75)
    
def spd_Sport():
    RightM.ChangeDutyCycle(100)
    LeftM.ChangeDutyCycle(100)
 
if __name__ == '__main__':
 while True:
   
   ret, frame = cam.read()
   cv2.imshow('frame', frame)
   
   k = cv2.waitKey(1)
   if k%256 == 27: #ESC
    print("Closing...")
    break
   elif k%256 == 32: #Space
    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name,frame)
    print("{} written!".format(img_name))
    img_counter += 1
   elif k%256 == ord('g'): # Change to grayscale
    #Reading Image
    gray_image = cv2.imread("opencv_frame_0.png", 0)
    print("Changing {} to grayscale!".format(img_name))
    cv2.imshow("Grayscale Image", gray_image)
   elif k%256 == ord('x'):
    #Closing grayscale window
    cv2.destroyWindow("Grayscale Image")
   
   for event in pygame.event.get():
   
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            print('Moving Forward')
            Forward()
        elif event.key == pygame.K_s:
            print('Moving Backwards')
            Backward()
        elif event.key == pygame.K_d:
            print('Turning Right')
            Right()
        elif event.key == pygame.K_a:
            print('Turning Left')
            Left()
            
        elif event.key == pygame.K_1:
            print('Speed = 50')
            spd_Eco()
        elif event.key == pygame.K_2:
            print('Speed = 75')
            spd_Comfort()
        elif event.key == pygame.K_3:
            print('Speed = 100')
            spd_Sport()
            
        # Set servo 1 angle
        elif event.key == pygame.K_DOWN:
            if S1_Angle <= 0:
                S1_Angle = 0
            else:
                S1_Angle-=5
            Servo.XiaoRGEEK_SetServoAngle(1,S1_Angle)
        elif event.key == pygame.K_UP:
            if S1_Angle >= 180:
                S1_Angle = 180
            else:
                S1_Angle+=5
            Servo.XiaoRGEEK_SetServoAngle(1,S1_Angle)
            
        # Set servo 2 angle
        elif event.key == pygame.K_i:
            if S2_Angle <= 0:
                S2_Angle = 0
            else:
                S2_Angle-=5
            Servo.XiaoRGEEK_SetServoAngle(2,S2_Angle)
        elif event.key == pygame.K_k:
            if S2_Angle >= 180:
                S2_Angle = 180
            else:
                S2_Angle+=5
            Servo.XiaoRGEEK_SetServoAngle(2,S2_Angle)
        
        # Set servo 3 angle
        elif event.key == pygame.K_RIGHT:
            if S3_Angle >= 180:
                S3_Angle = 180
            else:
                S3_Angle+=5
            Servo.XiaoRGEEK_SetServoAngle(3,S3_Angle)
        elif event.key == pygame.K_LEFT:
            if S3_Angle <= 0:
                S3_Angle = 0
            else:
                S3_Angle-=5
            Servo.XiaoRGEEK_SetServoAngle(3,S3_Angle)
            
        # Set servo 4 angle
        elif event.key == pygame.K_j:
            if S4_Angle <= 0:
                S4_Angle = 0
            else:
                S4_Angle-=5
            Servo.XiaoRGEEK_SetServoAngle(4,S4_Angle)
        elif event.key == pygame.K_l:
            if S4_Angle >= 90:
                S4_Angle = 90
            else:
                S4_Angle+=5
            Servo.XiaoRGEEK_SetServoAngle(4,S4_Angle)
            
        elif event.key == pygame.K_q:
            pygame.quit()
    elif event.type == pygame.KEYUP:
        print('no keys pressed')
        Stop()
        
cam.release()
cv2.destroyAllWindows()

 
