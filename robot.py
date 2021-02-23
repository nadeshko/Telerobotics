import os, sys
from KeyPress_Module import KeyPress
from RobotControl import Robot_Control, Robot_Camera


# Setup pygame
Kp = KeyPress()
# https://www.pygame.org/docs/ref/key.html

def main():
    '''
    Main function, sends Keyboard press to robot class
    '''
    window = True

    # Robot movement control
    if Kp.getKey('w'):
        Robot_Control('w')
    elif Kp.getKey('s'):
        Robot_Control('s')
    elif Kp.getKey('a'):
        Robot_Control('a')
    elif Kp.getKey('d'):
        Robot_Control('d')

    # Robot acceleration/decceleration
    elif Kp.getKey('LSHIFT'):
        Robot_Control('LSHIFT')
    elif Kp.getKey('LCTRL'):
        Robot_Control('LCTRL')

    # Robot Arm control, Servos 1-4
    elif Kp.getKey('KP4'):         # Servo 1
        Robot_Control('KP4')
    elif Kp.getKey('KP7'):
        Robot_Control('KP7')
    elif Kp.getKey('KP9'):         # Servo 2
        Robot_Control('KP9')
    elif Kp.getKey('KP6'):
        Robot_Control('KP6')
    elif Kp.getKey('KP3'):         # Servo 3
        Robot_Control('KP3')
    elif Kp.getKey('KP1'):
        Robot_Control('KP1')
    elif Kp.getKey('KP_MINUS'):    # Servo 4
        Robot_Control('KP_MINUS')
    elif Kp.getKey('KP_PLUS'):
        Robot_Control('KP_PLUS')

    # Camera control, Servos 7 & 8
    elif Kp.getKey('UP'):          # Servo 7
        Robot_Control('UP')
    elif Kp.getKey('DOWN'):
        Robot_Control('DOWN')
    elif Kp.getKey('LEFT'):        # Servo 8
        Robot_Control('LEFT')
    elif Kp.getKey('RIGHT'):
        Robot_Control('RIGHT')

    # Quit pygame and stop running code
    elif Kp.getKey('q'):
        print('quitting')
        window = False

    # When not pressing key, robot will stop
    else: Robot_Control('STOP')
    return window

if __name__ == '__main__':
    while True:
        window = main()
        Robot_Camera()
        camera = Robot_Camera().status
        if window == False or camera == False:
            break