import sys
from MpuModule import mpu
# DEBUG
Mpu = mpu("min_mx, max_mx, min_my, max_my")

def main():
    [ax,ay,angle] = Mpu.read_mpu()

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        sys.exit()