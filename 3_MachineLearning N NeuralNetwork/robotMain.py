from time import sleep
import RPi.GPIO as GPIO
import csv

def move(L_Spd = 0.6, R_Spd = 0.6):
    """
    Function for 360 robot movement based on keyboard presses
    """
    R_Spd *= 100
    L_Spd *= 100

    if R_Spd > 0:
        RightM.ChangeDutyCycle(R_Spd)
        GPIO.output(ENA, True)
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)
    elif R_Spd == 0:
        RightM.ChangeDutyCycle(0)
        GPIO.output(ENA, False)
        GPIO.output(IN1, False)
        GPIO.output(IN2, False)
    else:
        RightM.ChangeDutyCycle(-R_Spd)
        GPIO.output(ENA, True)
        GPIO.output(IN1, True)
        GPIO.output(IN2, False)

    if L_Spd > 0:
        LeftM.ChangeDutyCycle(L_Spd)
        GPIO.output(ENB, True)
        GPIO.output(IN3, False)
        GPIO.output(IN4, True)
    elif L_Spd == 0:
        LeftM.ChangeDutyCycle(0)
        GPIO.output(ENB, False)
        GPIO.output(IN3, False)
        GPIO.output(IN4, False)
    else:
        LeftM.ChangeDutyCycle(-L_Spd)
        GPIO.output(ENB, True)
        GPIO.output(IN3, True)
        GPIO.output(IN4, False)

if __name__ == '__main__':

    # Set GPIO call mode as BCM
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Define Ports
    ENA = 13
    ENB = 20
    IN1 = 19
    IN2 = 16
    IN3 = 21
    IN4 = 26
    R_Spd = 0
    L_Spd = 0

    # Port Setup
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

    # Specify the PWM control port and the frequency of the PWM signal
    RightM = GPIO.PWM(ENA, 1000)
    LeftM = GPIO.PWM(ENB, 1000)

    # Start PWM
    RightM.start(0)
    LeftM.start(0)

    # Import CSV file
    process = []
    with open("robot_control.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            process.append(row)

    # Seperate classes and frames
    classes, frames = [], []
    for a1, a2 in process:
        classes.append(a1)
        frames.append(a2)

    # Get time stamp and specific class
    action, time_stamp = [], []
    for index, element in enumerate(frames):
        if element == 0:
            time_stamp.append(frames[index - 1])
            action.append(classes[index - 1])
    # Append last action and time
    time_stamp.append(frames[-1])
    action.append(classes[-1])

    # Go through action list according to time stamp
    for i, Class in enumerate(action):
        # 30 km/hr, 30% duty cycle
        if Class == 0:
            print('moving at 30%')
            L_Spd, R_Spd = 0.3, 0.3
        # 50 km/hr, 50% duty cycle
        elif Class == 1:
            print('moving at 50%')
            L_Spd, R_Spd = 0.5, 0.5
        # 70 km/hr, 70% duty cycle
        elif Class == 2:
            print('moving at 70%')
            L_Spd, R_Spd = 0.7, 0.7
        # 80 km/hr, 80% duty cycle
        elif Class == 3:
            print('moving at 80%')
            L_Spd, R_Spd = 0.8, 0.8
        # 100 km/hr, 100% duty cycle
        elif Class == 4:
            print('moving at 100%')
            L_Spd, R_Spd = 1.0, 1.0
        # Stop, 0% duty cycle
        elif Class == 5:
            print('Stopping')
            R_Spd, L_Spd = 0.0, 0.0
        # Turning Right, higher duty cycle on left motor
        elif Class == 6:
            print('Turning Right')
            R_Spd = -R_Spd
            L_Spd = abs(L_Spd)
        # Turning Left, higher duty cycle on right motor
        elif Class == 7:
            print('Turning Left')
            L_Spd = -L_Spd
            R_Spd = abs(R_Spd)
        # Going straight, same positive duty cycle for both motor
        elif Class == 8:
            print('Going Straight')
            R_Spd = abs(R_Spd)
            L_Spd = abs(L_Spd)

        # action depending on Class
        move(L_Spd, R_Spd)
        # duration for action, assuming video is at 30 fps
        sleep(time_stamp[i]/30)

