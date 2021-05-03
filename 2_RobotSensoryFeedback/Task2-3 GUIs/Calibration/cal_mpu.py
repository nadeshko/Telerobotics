import FaBo9Axis_MPU9250
from time import sleep
import RPi.GPIO as GPIO
import numpy as np

# Global Values
Spd = 0.4

class mpu():
    def __init__(self):
        self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()
        self.mag = 0
        self.mx = []
        self.my = []
        self.avg_mx = []
        self.avg_my = []

        # Set GPIO call mode as BCM
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        ## Define Ports
        self.ENA = 13
        self.ENB = 20
        self.IN1 = 19
        self.IN2 = 16
        self.IN3 = 21
        self.IN4 = 26

        # Port Setup
        GPIO.setup(self.ENA, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.ENB, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN4, GPIO.OUT, initial=GPIO.LOW)

        # Specify the PWM control port and the frequency of the PWM signal
        self.RightM = GPIO.PWM(self.ENA, 1000)
        self.LeftM = GPIO.PWM(self.ENB, 1000)

        # Start PWM
        self.RightM.start(0)
        self.LeftM.start(0)

    def move(self, L_Spd=0.6, R_Spd=0.6):
        R_Spd *= 100
        L_Spd *= 100

        if R_Spd > 0:
            self.RightM.ChangeDutyCycle(R_Spd)
            GPIO.output(self.ENA, True)
            GPIO.output(self.IN1, False)
            GPIO.output(self.IN2, True)
        elif R_Spd == 0:
            self.RightM.ChangeDutyCycle(0)
            GPIO.output(self.ENA, False)
            GPIO.output(self.IN1, False)
            GPIO.output(self.IN2, False)
        else:
            self.RightM.ChangeDutyCycle(-R_Spd)
            GPIO.output(self.ENA, True)
            GPIO.output(self.IN1, True)
            GPIO.output(self.IN2, False)

        if L_Spd > 0:
            self.LeftM.ChangeDutyCycle(L_Spd)
            GPIO.output(self.ENB, True)
            GPIO.output(self.IN3, False)
            GPIO.output(self.IN4, True)
        elif L_Spd == 0:
            self.LeftM.ChangeDutyCycle(0)
            GPIO.output(self.ENB, False)
            GPIO.output(self.IN3, False)
            GPIO.output(self.IN4, False)
        else:
            self.LeftM.ChangeDutyCycle(-L_Spd)
            GPIO.output(self.ENB, True)
            GPIO.output(self.IN3, True)
            GPIO.output(self.IN4, False)

    def read_mag(self):
        global Spd

        for i in range (0,201,10):
            for j in range(0,11):
                sleep(0.2)
                self.mag = self.mpu9250.readMagnet()
                self.mx.append(self.mag['x'])
                self.my.append(self.mag['y'])
                if j > 3:
                    self.avg_mx.append((self.mx[j+i]+self.mx[j+i-1]+self.mx[j+i-2]+self.mx[j+i-3]+self.mx[j+i-4])/5)
                    self.avg_my.append((self.my[j+i]+self.my[j+i-1]+self.my[j+i-2]+self.my[j+i-3]+self.my[j+i-4])/5)
                print(j, i)
                sleep(0.2)
            self.move(Spd,-Spd)
            sleep(0.35)
            self.move(0,0)
            sleep(0.2)

        mx = np.asarray(self.mx)
        my = np.asarray(self.my)
        avg_mx = np.asarray(self.avg_mx)
        avg_my = np.asarray(self.avg_my)

        total_avg_mx = sum(mx)/len(mx)
        total_avg_my = sum(my)/len(my)

        print(total_avg_mx, total_avg_my)

        return mx, my, avg_mx, avg_my