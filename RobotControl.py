import RPi.GPIO as GPIO
from _XiaoRGEEK_SERVO_ import XR_Servo
import time
import numpy as np
import cv2

# Set GPIO call mode as BCM
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Initializing Servo for robot arms
Servo = XR_Servo()

# Define Ports
ENA = 13
ENB = 20
IN1 = 19
IN2 = 16
IN3 = 21
IN4 = 26

# Initial Values
Speed = 0
S1_Angle = 10
S2_Angle = 120
S3_Angle = 90
S4_Angle = 0
S7_Angle = 0
S8_Angle = 90
img_counter = 0
img = 0
x = 0
y = 0
angle = 0
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
RightM.start(Speed)
LeftM.start(Speed)

# Define movement functions
def Forward():
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
def Backward():
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
def Right():
    GPIO.output(ENA, True)
    GPIO.output(ENB, True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
def Left():
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

class Robot_Control():
    '''
    Robot Control with keyboard
    '''
    def __init__(self, key: str):
        global S1_Angle, S2_Angle, S3_Angle, S4_Angle, S7_Angle, S8_Angle, Speed

        # Robot Movements with WASD
        if key == 'w':
            Forward()
            print('Moving forward')
        elif key == 'd':
            Right()
            print('Turning right')
        elif key == 'a':
            Left()
            print('Turning left')
        elif key == 's':
            Backward()
            print('Moving backwards')
        elif key == 'STOP':
            Stop()

        # Accelerating and Deccelerating with LSHIFT and LCTRL, respectively
        elif key == 'LSHIFT':
            if Speed >= 100:
                Speed = 100
            else: Speed += 10
            RightM.ChangeDutyCycle(Speed)
            LeftM.ChangeDutyCycle(Speed)
        elif key == 'LCTRL':
            if Speed <= 0:
                Speed = 0
            else: Speed -= 10
            RightM.ChangeDutyCycle(Speed)
            LeftM.ChangeDutyCycle(Speed)

        # Servo 1 Control
        elif key == 'KP4':
            if S1_Angle <= 0:
                S1_Angle = 0
            else:
                S1_Angle -= 5
            Servo.XiaoRGEEK_SetServoAngle(1, S1_Angle)
        elif key == 'KP7':
            if S1_Angle >= 180:
                S1_Angle = 180
            else:
                S1_Angle += 5
            Servo.XiaoRGEEK_SetServoAngle(1, S1_Angle)
        # Servo 2 Control
        elif key == 'KP9':
            if S2_Angle <= 0:
                S2_Angle = 0
            else:
                S2_Angle -= 5
            Servo.XiaoRGEEK_SetServoAngle(2, S2_Angle)
        elif key == 'KP6':
            if S2_Angle >= 180:
                S2_Angle = 180
            else:
                S2_Angle += 5
            Servo.XiaoRGEEK_SetServoAngle(2, S2_Angle)
        # Servo 3 Control
        elif key == 'KP3':
            if S3_Angle >= 180:
                S3_Angle = 180
            else:
                S3_Angle += 5
            Servo.XiaoRGEEK_SetServoAngle(3, S3_Angle)
        elif key == 'KP1':
            if S3_Angle <= 0:
                S3_Angle = 0
            else:
                S3_Angle -= 5
            Servo.XiaoRGEEK_SetServoAngle(3, S3_Angle)
        # Servo 4 Control
        elif key == 'KP_MINUS':
            if S4_Angle <= 0:
                S4_Angle = 0
            else:
                S4_Angle -= 5
            Servo.XiaoRGEEK_SetServoAngle(4, S4_Angle)
        elif key == 'KP_PLUS':
            if S4_Angle >= 90:
                S4_Angle = 90
            else:
                S4_Angle += 5
            Servo.XiaoRGEEK_SetServoAngle(4, S4_Angle)

        # Camera control with arrow keys
        elif key == 'UP':
            if S7_Angle <= 0:
                S7_Angle = 0
            else:
                S7_Angle -= 5
            Servo.XiaoRGEEK_SetServoAngle(7, S7_Angle)
        elif key == 'DOWN':
            if S7_Angle >= 90:
                S7_Angle = 90
            else:
                S7_Angle += 5
            Servo.XiaoRGEEK_SetServoAngle(7, S7_Angle)
        elif key == 'LEFT':
            if S8_Angle <= 0:
                S8_Angle = 0
            else:
                S8_Angle -= 5
            Servo.XiaoRGEEK_SetServoAngle(8, S8_Angle)
        elif key == 'RIGHT':
            if S8_Angle >= 90:
                S8_Angle = 90
            else:
                S8_Angle += 5
            Servo.XiaoRGEEK_SetServoAngle(8, S8_Angle)

class Robot_Camera():
    def __init__(self):
        self.status = True
        ret, frame = cam.read()
        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)

        if k % 256 == 27:  # ESC
            print("Closing...")
            self.status = False
            cam.release()
            cv2.destroyAllWindows()
        elif k % 256 == 32:  # Space
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!\nPress g to grayscale, rotate and resize image!".format(img_name))
            img_counter += 1
        elif k % 256 == ord('g'):  # Change to grayscale
            # Reading Image
            img = input("which picture would you like to make grayscale?")
            gray_image = cv2.imread("opencv_frame_{}.png".format(img), 0)
            print("Changing opencv_frame_{}.png to grayscale!".format(img))
            # cv2.imshow("Grayscale Image", gray_image) # Debug

            y = int(input("what height would you want for the image?"))
            x = int(input("what length would you want for the image?"))
            print("resizing image to [{},{}]".format(x, y))
            numpy_image = np.asarray(gray_image)
            resize_image = cv2.resize(numpy_image, (x, y))

            rotate_image = cv2.rotate(resize_image, cv2.ROTATE_90_CLOCKWISE)
            cv2.imshow("Edited Image", rotate_image)

        elif k % 256 == ord('x'):  # Close and reset windows
            cv2.destroyAllWindows()