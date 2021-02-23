import os, sys
from KeyPress_Module import KeyPress

# Setup pygame
Kp = KeyPress()
# https://www.pygame.org/docs/ref/key.html

def main():
    window = True
    if Kp.getKey('w'):
        if Kp.getKey('d'):
            print('Moving north-east')
        elif Kp.getKey('a'):
            print('Moving north-west')
        else: print('Moving forward')
    elif Kp.getKey('s'):
        if Kp.getKey('d'):
            print('Moving south-east')
        elif Kp.getKey('a'):
            print('Moving south-west')
        else: print('Moving backwards')
    elif Kp.getKey('a'):
        print('Turning left')
    elif Kp.getKey('d'):
        print('Turning right')
    elif Kp.getKey('q'):
        print('quitting')
        window = False
    else:
        pass
    return window

if __name__ == '__main__':
    while True:
        window = main()
        if window == False:
            break


