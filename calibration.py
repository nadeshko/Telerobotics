import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
from matplotlib import style
import numpy as np
from time import sleep
import FaBo9Axis_MPU9250

SIZE = 2500
INTERVAL = 0.01

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

def animate(i):
    x = []
    y = []

    mag = mpu9250.readMagnet()
    mx = mag['x'] + 8
    my = mag['y'] + 16

    x.append(mx)
    y.append(my)

    ax1.scatter(x, y)

    if mx > 0 and my > 0:
        angle = np.rad2deg(np.arctan(my / mx))
    elif my < 0:
        angle = np.rad2deg(np.arctan(my / mx)) + 180
    elif mx < 0 and my > 0:
        angle = np.rad2deg(np.arctan(my / mx)) + 360
    elif mx == 1 and my == 0:
        angle = 90
    elif mx == -1 and my == 0:
        angle = 270
    print(round(angle, 2))


if __name__ == '__main__':
    fig = plt.figure(1)
    ax1 = fig.add_subplot(1,1,1)
    while True:
        ani = FuncAnimation(fig, animate, interval = 1000)
        plt.show()
