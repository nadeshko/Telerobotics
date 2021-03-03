import sys
from mpu_module import mpu
from cv2_module import openCV

mpu9250 = mpu()

def main():
        [x, y] = mpu9250.read_mpu()
        openCV(x,y)

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        sys.exit()
