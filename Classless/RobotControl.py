import RPi.GPIO as GPIO
from _XiaoRGEEK_SERVO_ import XR_Servo
import time
import Classless.KeyPressModule as Kp

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

def init():
    # Set GPIO call mode as BCM
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # Initializing Servo for robot arms
    Servo = XR_Servo()
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

def main():
    '''
    Main function, sends Keyboard press to robot class
    '''
    window = True

    # Robot movement control
    if Kp.getKey('w'):
        Forward()
        print('Moving forward')
    elif Kp.getKey('s'):
        Backward()
        print('Moving backward')
    elif Kp.getKey('a'):
        Left()
        print('Turning left')
    elif Kp.getKey('d'):
        Right()
        print('Turning right')

    # Accelerating and Deccelerating with LSHIFT and LCTRL, respectively
    elif Kp.getKey('LSHIFT'):
        if Speed >= 100:
            Speed = 100
        else:
            Speed += 10
        RightM.ChangeDutyCycle(Speed)
        LeftM.ChangeDutyCycle(Speed)
    elif Kp.getKey('LCTRL'):
        if Speed <= 0:
            Speed = 0
        else:
            Speed -= 10
        RightM.ChangeDutyCycle(Speed)
        LeftM.ChangeDutyCycle(Speed)

    elif Kp.getKey('q'):
        print('Quitting')
        window = False

    else: Stop()

    return window