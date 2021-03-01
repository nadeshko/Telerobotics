# failed
from hcsr04sensor import sensor
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

def main():
 GPIO.setmode(GPIO.BCM)

 TRIG = 17
 ECHO = 27

 GPIO.setup(TRIG, GPIO.OUT)
 GPIO.setup(ECHO, GPIO.IN)


 
 value = sensor.Measurement(TRIG, ECHO)
 raw_measurement = value.raw_distance()
 
 print('Measuring...')
 print('The Distance = {} centimeters'.format(round(raw_measurement, 1)))

while True:
 main()