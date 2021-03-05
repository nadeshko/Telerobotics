import sys
from mpu_module import mpu
from cv2_module import openCV
from plot_module import plot

mpu9250 = mpu()

def main():
        [x, y,mx,my] = mpu9250.read_mpu()
        openCV(x,y)
        plot(mx,my
        # time(0.5)

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        sys.exit()
