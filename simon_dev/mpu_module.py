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
        '''
        self.mx_N = []
        self.my_N = []
        self.mx_E = []
        self.my_E = []
        self.mx_S = []
        self.my_S = []
        self.mx_W = []
        self.my_W = []'''

    def read_mpu(self):
        self.accel = self.mpu9250.readAccel()
        self.gyro = self.mpu9250.readGyro()

        for i in range (0,200):
            self.mag = self.mpu9250.readMagnet()
            self.mx.append(self.mag['x'])
            self.my.append(self.mag['y'])
            print(i)
            sleep(0.25)
            i += 1
            if i > 4:
                self.avg_mx.append((self.mx[i-5] + self.mx[i - 1] + self.mx[i - 2] + self.mx[i - 3] + self.mx[i - 4])/ 5)
                self.avg_my.append((self.my[i-5] + self.my[i - 1] + self.my[i - 2] + self.my[i - 3] + self.my[i - 4])/ 5)

        mx = np.asarray(self.mx)
        my = np.asarray(self.my)
        avg_mx = np.asarray(self.avg_mx)
        avg_my = np.asarray(self.avg_my)
        '''
        for i in range (0,50):
            self.mag = self.mpu9250.readMagnet()
            self.mx_N.append(self.mag['x'])
            self.my_N.append(self.mag['y'])
            sleep(0.25)
            print(i)
            i+=1
            mx_N = np.asarray(self.mx_N)
            my_N = np.asarray(self.my_N)
        avg_mxN = sum(mx_N) / 50
        avg_myN = sum(my_N) / 50
        sleep(5)
        i = 0
        for i in range (0,50):
            self.mag = self.mpu9250.readMagnet()
            self.mx_E.append(self.mag['x'])
            self.my_E.append(self.mag['y'])
            sleep(0.25)
            print(i)
            i+=1
            mx_E = np.asarray(self.mx_E)
            my_E = np.asarray(self.my_E)
        avg_mxE = sum(mx_E) / 50
        avg_myE = sum(my_E) / 50
        sleep(5)
        i = 0
        for i in range(0, 50):
            self.mag = self.mpu9250.readMagnet()
            self.mx_S.append(self.mag['x'])
            self.my_S.append(self.mag['y'])
            sleep(0.25)
            print(i)
            i += 1
            mx_S = np.asarray(self.mx_S)
            my_S = np.asarray(self.my_S)
        avg_mxS = sum(mx_S) / 50
        avg_myS = sum(my_S) / 50
        sleep(5)
        i = 0
        for i in range(0, 50):
            self.mag = self.mpu9250.readMagnet()
            self.mx_W.append(self.mag['x'])
            self.my_W.append(self.mag['y'])
            sleep(0.25)
            print(i)
            i += 1
            mx_W = np.asarray(self.mx_W)
            my_W = np.asarray(self.my_W)
        avg_mxW = sum(mx_W) / 50
        avg_myW = sum(my_W) / 50

        mx = np.concatenate((mx_N,mx_E,mx_S,mx_W))
        my = np.concatenate((my_N,my_E,my_S,my_W))
        avg_mx_list = [avg_mxN, avg_mxE, avg_mxS, avg_mxW]
        avg_my_list = [avg_myN, avg_myE, avg_myS, avg_myW]
        avg_mx = np.asarray(avg_mx_list)
        avg_my = np.asarray(avg_my_list)'''

        '''
        print(" ax = " , ( self.accel['x'] ))
        print(" ay = " , ( self.accel['y'] ))
        print(" az = " , ( self.accel['z'] ))

        print(" gx = " , ( self.gyro['x'] ))
        print(" gy = " , ( self.gyro['y'] ))
        print(" gz = " , ( self.gyro['z'] ))
        
        print(" mx = " , ( self.mag['x'] ))
        print(" my = " , ( self.mag['y'] ))
        #print(" mz = " , ( self.mag['z'] ))'''

        a_x = self.accel['x']
        a_y = self.accel['y']

        x1 = 256 + 256 * a_x
        y1 = 256 - 256 * a_y
        
        x = round(x1)
        y = round(y1)

        #sleep(0.5)

        return x,y,mx,my, avg_mx, avg_my