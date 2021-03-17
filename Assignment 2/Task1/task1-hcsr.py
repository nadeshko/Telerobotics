from time import sleep, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ECHO = 4
TRIG = 17

GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def get_distance():
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

    dis = int((t2 - t1) * 340 / 2 * 100)
    if dis < 255:
        print(f"Distance: {dis} cm")
    return dis

if __name__ == '__main__':
    while True:
        get_distance()