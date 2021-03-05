import sys
from time import sleep
from mpu_module import mpu
from cv2_module import openCV

mpu9250 = mpu()
OpenCV = openCV()

def main():
        [x, y] = mpu9250.read_mpu()
        OpenCV.position(x,y)
        sleep(0.2)

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        sys.exit()
