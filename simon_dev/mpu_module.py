import FaBo9Axis_MPU9250
from time import sleep
import numpy as np

class mpu():
    def __init__(self):
        self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()
        self.accel = 0
        self.gyro = 0
        self.mag = 0
        self.mx = []
        self.my = []
        self.avg_mx = []
        self.avg_my = []

    def read_accel(self):
        self.accel = self.mpu9250.readAccel()
        print(" ax = ", (self.accel['x']))
        print(" ay = ", (self.accel['y']))
        print(" az = ", (self.accel['z']))
        x = round(256 + (256 * self.accel['x']))
        y = round(256 - (256 * self.accel['y']))
        sleep(0.5)

        return x, y

    def read_mag(self):

        for i in range (0,200):
            self.mag = self.mpu9250.readMagnet()
            self.mx.append(self.mag['x'])
            self.my.append(self.mag['y'])
            if i%3 == 0 and i > 3:
                self.avg_mx.append((self.mx[i] + self.mx[i - 1] + self.mx[i-2] + self.mx[i-3] + self.mx[i-4]) / 5)
                self.avg_my.append((self.my[i] + self.my[i - 1] + self.my[i-2] + self.my[i-3] + self.my[i-4]) / 5)
            print(i)
            i += 1
            sleep(0.25)

        mx = np.asarray(self.mx)
        my = np.asarray(self.my)
        avg_mx = np.asarray(self.avg_mx)
        avg_my = np.asarray(self.avg_my)

        return mx, my, avg_mx, avg_my

    def read_gyro(self):
        self.gyro = self.mpu9250.readGyro()