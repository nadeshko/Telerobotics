import sys
from MpuModule import mpu
# DEBUG
Mpu = mpu(0,0,0,0)

def main():
    '''
    Takes MPU data and displays real-time tracking
    '''
    [ax,ay,angle] = Mpu.read_mpu()

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        sys.exit()