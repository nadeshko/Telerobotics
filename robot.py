import os, sys
from KeyPress_Module import KeyPress
from RobotControl import Robot_Control

# Setup pygame
Kp = KeyPress()
# https://www.pygame.org/docs/ref/key.html

def main():
    window = True

    if Kp.getKey('w'):
        if Kp.getKey('d'):
            Robot_Control('wd')
        elif Kp.getKey('a'):
            Robot_Control('wa')
        else: Robot_Control('w')
    elif Kp.getKey('s'):
        if Kp.getKey('d'):
            Robot_Control('sd')
        elif Kp.getKey('a'):
            Robot_Control('sa')
        else: Robot_Control('s')
    elif Kp.getKey('a'):
        Robot_Control('a')
    elif Kp.getKey('d'):
        Robot_Control('d')
    elif Kp.getKey('LSHIFT'):
        Robot_Control('LSHIFT')
    elif Kp.getKey('q'):
        print('quitting')
        window = False
    else:
        Robot_Control('STOP')
    return window

if __name__ == '__main__':
    while True:
        window = main()
        if window == False:
            break