import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define  Port and defualt duty cycle of PWM
ENA=13
Speed=50

# Specify the PWM control port and the frequency of the PWM signal
PWM=GPIO.PWM(ENA,1000)

# Start PWMPWM.start(0)
PWM.start(0)

# Change the duty cycle to 55
Speed+=5
PWM.ChangeDutyCycle(Speed)

# Stop PWM
PWM.stop()