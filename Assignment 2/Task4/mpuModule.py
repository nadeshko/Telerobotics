import FaBo9Axis_MPU9250
from time import sleep
import numpy as np
from math import pi

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

    def read_mag(self):
        '''
        Returns Magnetometer data every 0.2 sec
        '''
        mag = self.mpu9250.readMagnet()
        mx = mag['x'] + 3.4
        my = mag['y'] + 8.8
        hdg = np.arctan2(-my,mx)*180/pi
        if hdg < 0:
            hdg += 360
        print(hdg)

        '''acc = self.mpu9250.readAccel()

        x = acc['x']
        y = acc['y']
        z = acc['z']

        roll = np.rad2deg(np.arctan2(x,math.sqrt(z*z + y*y)))
        pitch = np.rad2deg(np.arctan2(z,np.sign(y)*math.sqrt((0.01*x*x)+(y*y))))

        yaw = np.rad2deg(np.arctan2(z,math.sqrt(x*x + z*z)))

        print(f"ax = {acc['x']}")
        print(f"ay = {acc['y']}")
        print(f"az = {acc['z']}\n")

        print(f"Yaw = {yaw}, Roll = {roll}, Pitch = {pitch}\n")'''


        #heading = np.rad2deg(np.arctan2(mag['y'],mag['x']))
        # Normalize mx and my to [-1,1]
        #mx = ((2*mag['x'] - self.min_mx - self.max_mx) / abs((self.max_mx - self.min_mx)))
        #my = ((2*mag['y'] - self.min_my - self.max_my) / abs((self.max_my - self.min_my)))
        #mx = 2 * ((mag['x'] - self.min_mx) / (self.max_mx - self.min_mx)) - 1
        #my = 2 * ((mag['y'] - self.min_my) / (self.max_my - self.min_my)) - 1
        '''
        if mx > 0 and my > 0:
            angle = np.rad2deg(np.arctan(mx / my))
        elif my < 0:
            angle = np.rad2deg(np.arctan(mx / my)) + 180
        elif mx < 0 and my > 0:
            angle = np.rad2deg(np.arctan(mx / my)) + 360
        elif mx==1 and my==0:
            angle = 90
        elif mx==-1 and my==0:
            angle = 270

        angle = 360 - angle
        
        if mx > 0 :
            heading = np.rad2deg(np.arctan2(mx, my))
            print(mx)
        elif mx < 0:
            if my >= 0:
                heading = np.rad2deg(np.arctan2(my, mx))
                print(f"positive {my}")
            elif my < 0:
                heading = np.rad2deg(np.arctan2(my, mx))
                print(f"negative {my}")'''

        #print(f"{angle} {heading}")
        #print(f"heading {angle} {mx} {my} {mag['x']} {mag['y']} {mag['z']}")
        sleep(0.2)

        #return mx, my