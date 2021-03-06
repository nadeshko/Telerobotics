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
    ### STRAIGHT START ###
    move(0.5, 0.5)
    sleep(1.5)
    move(0, 0)
    sleep(1)
    a1 = Mpu.read_mag()
    while a1 > 160:
        move(0.5, -0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)
        a1 = Mpu.read_mag()
    while a1 < 155:
        move(-0.5, +0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)
        a1 = Mpu.read_mag()

    move(0.8, 0.8)
    sleep(0.5)
    move(0, 0)
    sleep(1)
    ### STRAIGHT END ###

def square():
    ### SQUARE START ###
    move(0.5, 0.5)
    sleep(2)
    move(0, 0)
    sleep(1)
    a1 = Mpu.read_mag()
    while a1 > 250 or a1 < 240:
        a1 = Mpu.read_mag()
        move(0.5, -0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)

    move(0.5, 0.5)
    sleep(2)
    move(0, 0)
    sleep(1)
    a2 = Mpu.read_mag()
    while a2 >325 or a2 < 300:
        a2 = Mpu.read_mag()
        move(0.5, -0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)

    move(0.5, 0.5)
    sleep(2)
    move(0, 0)
    sleep(1)
    a3 = Mpu.read_mag()
    while a3 > 188 or a3 < 160:
        a3 = Mpu.read_mag()
        move(0.5, -0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)

    move(0.5, 0.5)
    sleep(2)
    move(0, 0)
    sleep(1)
    ### SQUARE END ###

def circle():
    ### CIRCLE START ###
    #starting point
    move(0.6, 0.3)
    sleep(2.15)
    move(0, 0)
    sleep(1)
    a1 = Mpu.read_mag()
    #first check point
    while a1 > 325:
        move(0.5, -0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)
        a1 = Mpu.read_mag()
    while a1 < 310:
        move(-0.5, +0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)
        a1 = Mpu.read_mag()
    #altered -> move
    move(0.6, 0.3)
    sleep(2.15)
    move(0, 0)
    sleep(1)
    a2 = Mpu.read_mag()
    #second check point
    while a1 > 290:
        move(0.5, -0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)
        a1 = Mpu.read_mag()
    while a1 < 280:
        move(-0.5, +0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)
        a1 = Mpu.read_mag()
    #altered -> move
    move(0.6, 0.3)
    sleep(2.15)
    move(0, 0)
    sleep(1)
    a3 = Mpu.read_mag()
    while a1 > 180:
        move(0.5, -0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)
        a1 = Mpu.read_mag()
    while a1 < 170:
        move(-0.5, +0.5)
        sleep(0.15)
        move(0, 0)
        sleep(1)
        a1 = Mpu.read_mag()

    move(0.6, 0.3)
    sleep(2.15)
    move(0, 0)
    sleep(1)
    ### CIRCLE END ###

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
    #square()
    circle()