import sys
from cal_mpu import mpu
from cal_plot import plot

mpu9250 = mpu()

def main():
        [mx, my, avg_mx, avg_my] = mpu9250.read_mag()
        plot(mx,my,avg_mx,avg_my)

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        sys.exit()
