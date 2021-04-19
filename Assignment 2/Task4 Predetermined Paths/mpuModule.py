import FaBo9Axis_MPU9250
import numpy as np

class mpu():
    def __init__(self):
        '''
        Calls MPU9250 module
        '''
        self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()

    def read_mag(self):
        '''
        Returns Magnetometer data every 0.25 sec
        '''
        mag = self.mpu9250.readMagnet()
        # Normalize mx and my to [-1,1]

        mx = mag['x'] + 8
        my = mag['y'] + 16

        if mx > 0 and my > 0:
            angle = np.rad2deg(np.arctan(my / mx))
        elif my < 0:
            angle = np.rad2deg(np.arctan(my / mx)) + 180
        elif mx < 0 and my > 0:
            angle = np.rad2deg(np.arctan(my / mx)) + 360
        elif mx == 1 and my == 0:
            angle = 90
        elif mx == -1 and my == 0:
            angle = 270
        angle = round(angle, 2)

        print(f"{angle} degrees")

        return angle