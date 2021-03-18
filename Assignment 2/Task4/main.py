import RPi.GPIO as GPIO
from mpuModule import mpu

def main():
    Mpu.read_mag()

    #(ITS TURNING RIGHT, MUST TURN LEFT)
    '''if angle > 155:
        err = angle - 155
        print(f"error = {err}")
        move(Spd + abs(err) * 0.6, Spd - abs(err) * 0.11)
    elif angle < 155:
        err = angle - 155
        print(f"error = {err}")
        move(Spd - abs(err) * 0.11, Spd + abs(err) * 0.6)
    else:
        move(Spd, Spd)'''

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

    #           min mx   max mx   min my  max my
    Mpu = mpu(-26.1666, 40.1818, -63.947, 4.3732)
    '''
    # MOVE 1: 90 for 0.75 second
    move(90,90)
    sleep(1.25)
    move(0,0) # Stops
    sleep(1)
    angle = Mpu.read_mag()
    print(angle)
    if angle > 155:
        err = angle - 155
        print(f"error = {err}")
        move(60 + abs(err)*0.01, 60 - abs(err) * 0.9)
    elif angle < 155:
        err = angle - 155
        print(f"error = {err}")
        move(60 - abs(err) * 0.75, 60 + abs(err)*0.01)
    sleep(1)

    # MOVE 2: 40 for 2.5 sec
    move(40,40)
    sleep(2)
    move(0,0)
    sleep(1)
    angle = Mpu.read_mag()
    print(angle)
    if angle > 155:
        err = angle - 155
        print(f"error = {err}")
        move(60 + abs(err)*0.01, 60 - abs(err) * 0.9)
    elif angle < 155:
        err = angle - 155
        print(f"error = {err}")
        move(60 - abs(err) * 0.75, 60 + abs(err)*0.01)
    sleep(1)

    move(75,75)
    sleep(1.35)
    move(0, 0)
    sleep(1)'''

    while True:
        main()
