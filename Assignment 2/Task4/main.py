import RPi.GPIO as GPIO
from mpuModule import mpu

def main():
    angle = Mpu.read_mag()

if __name__ == '__main__':
    # Set GPIO call mode as BCM
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

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

    Mpu = mpu(-7.5634, 20.5034, -34.7336, -6.7746)

    while True:
        main()
