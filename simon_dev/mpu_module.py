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
        '''
        self.mag = self.mpu9250.readMagnet()
        mx = 2 * ((self.mag['x'] + 6.0938) / (18.962 + 6.2938)) - 1
        my = 2 * ((self.mag['y'] + 43.9458) / (-19.6428 + 43.9458)) - 1

        #print(mx, my)
        #angle = np.rad2deg(np.arctan(mx / my)) - 20


        if mx > 0 and my > 0:
            angle = np.rad2deg(np.arctan(my/ mx))
        #elif mx > 0 and my < 0:
            #angle = np.rad2deg(np.arctan(my / mx)) + 90
        #elif mx < 0 and my < 0:
            #angle = np.rad2deg(np.arctan(mx / my)) + 180
        #elif mx < 0 and my > 0:
            #angle = 360 - np.rad2deg(np.arctan(mx / my))
        print(angle)'''

    def read_gyro(self):
        self.gyro = self.mpu9250.readGyro()