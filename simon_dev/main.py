import sys
from time import sleep
from mpu_module import mpu
#from cv2_module import openCV
from plot_module import plot

mpu9250 = mpu()

def main():
        [x, y, mx, my, avg_mx, avg_my] = mpu9250.read_mpu()
        #openCV(x,y)
        plot(mx,my,avg_mx,avg_my)

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        sys.exit()
