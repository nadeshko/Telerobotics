import FaBo9Axis_MPU9250
from time import sleep
import numpy as np

class mpu():
    def __init__(self, min_mx, max_mx, min_my, max_my):
        '''
        Calls MPU9250 module
        '''
        self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()
        self.min_mx = min_mx
        self.max_mx = max_mx
        self.min_my = min_my
        self.max_my = max_my

    def read_mpu(self):
        '''
        Returns MPU data every 0.25 sec
        '''
        accel = self.mpu9250.readAccel()
        ax = round(240 + (240 * accel['x']))
        ay = round(240 - (240 * accel['y']))

        mag = self.mpu9250.readMagnet()
        mx = 2 * ((mag['x'] - self.min_mx) / (self.max_mx - self.min_mx)) - 1
        my = 2 * ((mag['y'] - self.min_my) / (self.max_my - self.min_my)) - 1

        if mx > 0 and my > 0:
            angle = np.rad2deg(np.arctan(mx / my))
        elif my < 0:
            angle = np.rad2deg(np.arctan(mx / my)) + 180
        elif mx < 0 and my > 0:
            angle = np.rad2deg(np.arctan(mx / my)) + 360
        elif mx == 1 and my == 0:
            angle = 90
        elif mx == -1 and my == 0:
            angle = 270

        print(angle) # DEBUG
        sleep (0.2)

        return ax,ay,angle