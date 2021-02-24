from KeyPress_Module import KeyPress
from MotorModule import Motor_Control
from ServoModule import Servo_control
from CameraModule import Camera

###########################################################################
###                             ROBOT MAIN                              ###
###########################################################################

# Initialize pygame
Kp = KeyPress()
# Define motor ports
motor = Motor_Control(13, 20, 19, 16, 21, 26)
# Initializing Servo Angles
servo = Servo_control(0, 120, 90, 0, 0, 90)
# Starting Camera
camera = Camera()

def main():
    '''
    Main function, sends Keyboard press to robot classes
    '''
    close = True
    Speed = 0

    # Show Camera window
    camera.open()

    # Robot acceleration/decceleration
    if Kp.getKey('LSHIFT'):
        if Speed >= 1:
            Speed = 1
        else:
            Speed += 0.1
    elif Kp.getKey('LCTRL'):
        if Speed <= 0:
            Speed = 0
        else:
            Speed -= 0.1

    # Robot Movements with WASD
    elif Kp.getKey('w'):
        motor.Forward(Speed, 0)
        print('Moving forward')
    elif Kp.getKey('s'):
        motor.Backward(Speed, 0)
        print('Turning right')
    elif Kp.getKey('a'):
        motor.Left(Speed)
        print('Turning left')
    elif Kp.getKey('d'):
        motor.Right(Speed)
        print('Moving backwards')

    # Servo 1 Control
    elif Kp.getKey('KP4'):
        servo.down(1)
    elif Kp.getKey('KP7'):
        servo.up(1)
    # Servo 2 Control
    elif Kp.getKey('KP9'):
        servo.down(2)
    elif Kp.getKey('KP6'):
        servo.up(2)
    # Servo 3 Control
    elif Kp.getKey('KP1'):
        servo.down(3)
    elif Kp.getKey('KP3'):
        servo.up(3)
    # Servo 4 Control
    elif Kp.getKey('KP_MINUS'):
        servo.down(4)
    elif Kp.getKey('KP_PLUS'):
        servo.up(4)
    # Servo 7 Control
    elif Kp.getKey('UP'):
        servo.down(7)
    elif Kp.getKey('DOWN'):
        servo.up(7)
    # Servo 8 Control
    elif Kp.getKey('LEFT'):
        servo.down(8)
    elif Kp.getKey('RIGHT'):
        servo.up(8)

    elif Kp.getKey('ESC'):
        print("quitting...")
        camera.close()
        close = False
    else:
        motor.Stop()
    return close

if __name__ == '__main__':
    while True:
        close = main()
        if close == False:
            break