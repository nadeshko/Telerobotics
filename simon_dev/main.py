import sys
from mpu_module import mpu
#from cv2_module import openCV
from plot_module import plot

mpu9250 = mpu()
#OpenCV = openCV()

def main():
        #[x ,y] = mpu9250.read_accel()
        #OpenCV.Elec_lvl(x, y)

        [mx, my, avg_mx, avg_my] = mpu9250.read_mag()
        plot.calibrate(mx,my,avg_mx,avg_my)
        #OpenCV.Elec_compass(angle)

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        sys.exit()
