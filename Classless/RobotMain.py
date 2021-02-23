import Classless.KeyPressModule as Kp
import Classless.RobotControl as Robot_Control

Kp.init()
Robot_Control.init()

def main():
    window = Robot_Control.main()
    return window

if __name__ == '__main__':
    while True:
        py = main()
        if py == False:
            break