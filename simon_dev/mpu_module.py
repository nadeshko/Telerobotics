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

    def read_accel(self, Read):
        while Read == True:
            self.accel = self.mpu9250.readAccel()
            x = round(256 + (256 * self.accel['x']))
            y = round(256 - (256 * self.accel['y']))
            sleep(1)

        return x, y

    def read_mag(self):
        for i in range (0,200):
            self.mag = self.mpu9250.readMagnet()
            self.mx.append(self.mag['x'])
            self.my.append(self.mag['y'])
            print(i)
            sleep(0.25)
            i += 1

        for i in range (2,4,198):
            self.avg_mx.append((self.mx[i - 2] + self.mx[i - 1] + self.mx[i] + self.mx[i + 1] + self.mx[i + 2])/ 5)
            self.avg_my.append((self.my[i - 2] + self.my[i - 1] + self.my[i] + self.my[i + 1] + self.my[i + 2])/ 5)

        mx = np.asarray(self.mx)
        my = np.asarray(self.my)
        avg_mx = np.asarray(self.avg_mx)
        avg_my = np.asarray(self.avg_my)

        return mx, my, avg_mx, avg_my

    def read_gyro(self):
        self.gyro = self.mpu9250.readGyro()



'''
        self.mx_N = []
        self.my_N = []
        self.mx_E = []
        self.my_E = []
        self.mx_S = []
        self.my_S = []
        self.mx_W = []
        self.my_W = []
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
        avg_my = np.asarray(avg_my_list)

       
        print(" ax = " , ( self.accel['x'] ))
        print(" ay = " , ( self.accel['y'] ))
        print(" az = " , ( self.accel['z'] ))

        print(" gx = " , ( self.gyro['x'] ))
        print(" gy = " , ( self.gyro['y'] ))
        print(" gz = " , ( self.gyro['z'] ))
        
        print(" mx = " , ( self.mag['x'] ))
        print(" my = " , ( self.mag['y'] ))
        #print(" mz = " , ( self.mag['z'] ))'''



