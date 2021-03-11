import FaBo9Axis_MPU9250
from time import sleep
import numpy as np

class mpu():
    def __init__(self, min_mx, max_mx, min_my, max_my):
        self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()
        self.min_mx = min_mx
        self.max_mx = max_mx
        self.min_my = min_my
        self.max_my = max_my

    def read_mpu(self):
        accel = self.mpu9250.readAccel()
        ax = round(256 + (256 * accel['x']))
        ay = round(256 - (256 * accel['y']))

        mag = self.mpu9250.readMagnet()
        # Normalize to [-1,1]
        mx = 2 * ((mag['x'] - self.min_mx) / (self.max_mx - self.min_mx)) - 1
        my = 2 * ((mag['y'] - self.min_my) / (self.max_my - self.min_my)) - 1

        angle = np.rad2deg(np.arctan(mx / my))

        '''
        if mx > 0 and my > 0:
            angle = np.rad2deg(np.arctan(my / mx))
        elif mx > 0 and my < 0:
            angle = np.rad2deg(np.arctan(my / mx)) + 90
        elif mx < 0 and my < 0:
            angle = np.rad2deg(np.arctan(mx / my)) + 180
        elif mx < 0 and my > 0:
            angle = 360 - np.rad2deg(np.arctan(mx / my))'''

        print(angle)
        sleep(0.25)

        return ax,ay,angle