import FaBo9Axis_MPU9250
from time import sleep

class mpu():
    def __init__(self):
        self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()
        self.accel = 0
        self.gyro = 0
        self.mag = 0

    def read_mpu(self):
        self.accel = self.mpu9250.readAccel()
        self.gyro = self.mpu9250.readGyro()
        self.mag = self.mpu9250.readMagnet()
        print(" ax = " , ( self.accel['x'] ))
        print(" ay = " , ( self.accel['y'] ))
        print(" az = " , ( self.accel['z'] ))

        print(" gx = " , ( self.gyro['x'] ))
        print(" gy = " , ( self.gyro['y'] ))
        print(" gz = " , ( self.gyro['z'] ))

        print(" mx = " , ( self.mag['x'] ))
        print(" my = " , ( self.mag['y'] ))
        print(" mz = " , ( self.mag['z'] ))

        a_x = self.accel['x']
        a_y = self.accel['y']

        x1 = 256 + 256 * a_x
        y1 = 256 - 256 * a_y
        
        mx = self.mag['x']
        my = self.mag['y']
        
        x = round(x1)
        y = round(y1)

        sleep(0.5)

        return x,y,mx,my