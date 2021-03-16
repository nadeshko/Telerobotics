import FaBo9Axis_MPU9250
from time import sleep
import numpy as np

class mpu():
    def __init__(self):
        self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()
        self.mag = 0
        self.mx = []
        self.my = []
        self.avg_mx = []
        self.avg_my = []

    def read_mag(self):
        for i in range (0,200):
            self.mag = self.mpu9250.readMagnet()
            self.mx.append(self.mag['x'])
            self.my.append(self.mag['y'])
            if i > 3:
                self.avg_mx.append((self.mx[i]+self.mx[i-1]+self.mx[i-2]+self.mx[i-3]+self.mx[i-4])/5)
                self.avg_my.append((self.my[i]+self.my[i-1]+self.my[i-2]+self.my[i-3]+self.my[i-4])/5)
            print(i)
            i += 1
            sleep(0.15)

        mx = np.asarray(self.mx)
        my = np.asarray(self.my)
        avg_mx = np.asarray(self.avg_mx)
        avg_my = np.asarray(self.avg_my)

        total_avg_mx = sum(mx)/len(mx)
        total_avg_my = sum(my)/len(my)

        print(total_avg_mx, total_avg_my)

        return mx, my, avg_mx, avg_my