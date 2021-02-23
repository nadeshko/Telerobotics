import RPi.GPIO as GPIO
from _XiaoRGEEK_SERVO_ import XR_Servo
from time import sleep

class Robot_Control():
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
    Speed = 0
    S1_Angle = 10
    S2_Angle = 120
    S3_Angle = 90
    S4_Angle = 0
    img_counter = 0
    Servo.XiaoRGEEK_SetServoAngle(1, S1_Angle)
    Servo.XiaoRGEEK_SetServoAngle(2, S2_Angle)
    Servo.XiaoRGEEK_SetServoAngle(3, S3_Angle)
    Servo.XiaoRGEEK_SetServoAngle(4, S4_Angle)

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
    RightM.start(0)
    LeftM.start(0)

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

    def __init__(self, key: str):
        Speed = 0

        if key == 'w':
            Forward()
            print('Moving forward')
        elif key == 'wd':
            print('Moving north-east')
        elif key == 'wa':
            print('Moving north-west')
        elif key == 'd':
            Right()
            print('Turning right')
        elif key == 'a':
            Left()
            print('Turning left')
        elif key == 's':
            Backward()
            print('Moving backwards')
        elif key == 'sa':
            print('Moving south-west')
        elif key == 'sd':
            print('Moving south-east')

        elif key == 'STOP':
            Stop()




