import FaBo9Axis_MPU9250
import time
import sys
import cv2
import numpy as np
from OpenCV import OpenCV

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

try:
    while True:
        accel = mpu9250.readAccel()
        a_x = accel['x']
        a_y = accel['y']
        
        x = 256 + 256*a_x
        y = 256 + 256*a_y
        
        time.sleep(1)
        return x,y

OpenCV(x,y)

except KeyboardInterrupt:
    sys.exit()
