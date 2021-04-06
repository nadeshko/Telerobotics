from mpuModule import mpu
import RPi.GPIO as GPIO
from time import sleep

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

def straight():
    pass

def square():
    move(0.5, 0.5)
    sleep(2)
    move(0, 0)
    sleep(1)
    angle = Mpu.read_mag()
    while angle > 250 or angle < 240:
        angle = Mpu.read_mag()
        move(0.5, -0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)

    move(0.5, 0.5)
    sleep(2)
    move(0, 0)
    sleep(1)
    angle = Mpu.read_mag()
    while angle >325 or angle < 300:
        angle = Mpu.read_mag()
        move(0.5, -0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)

    move(0.5, 0.5)
    sleep(2)
    move(0, 0)
    sleep(1)
    angle = Mpu.read_mag()
    while angle > 188 or angle < 160:
        angle = Mpu.read_mag()
        move(0.5, -0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)

    move(0.5, 0.5)
    sleep(2)
    move(0, 0)
    sleep(1)
    angle = Mpu.read_mag()

def circle():
    pass

if __name__ == '__main__':
    # Set GPIO call mode as BCM
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    Err = False

    ## Define Ports
    ENA = 13
    ENB = 20
    IN1 = 19
    IN2 = 16
    IN3 = 21
    IN4 = 26

    # Port Setup
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

    Mpu = mpu()

    # Comment and uncomment these to change functions
    #straight()
    square()
    #circle()