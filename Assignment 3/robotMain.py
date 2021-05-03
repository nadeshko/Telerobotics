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
    results = []
    with open("robot_control.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            results.append(row)

    # Seperate classes and frames
    classes, frames = [], []
    for x, y in results:
        classes.append(x)
        frames.append(y)

    # Get time stamp and specific class
    action, time_stamp = [], []
    for index, elem in enumerate(frames):
        if elem == 0:
            time_stamp.append(frames[index - 1])
            action.append(classes[index - 1])
    time_stamp.append(frames[-1]) # Append last action
    action.append(classes[-1])

    # Go through action list according to time stamp
    for i, label in enumerate(action):
        if label == 0:
            print('moving at 30%')
            L_Spd, R_Spd = 0.35, 0.35
        elif label == 1:
            print('moving at 50%')
            L_Spd, R_Spd = 0.4, 0.4
        elif label == 2:
            print('moving at 70%')
            L_Spd, R_Spd = 0.7, 0.7
        elif label == 3:
            print('moving at 80%')
            L_Spd, R_Spd = 0.8, 0.8
        elif label == 4:
            print('moving at 100%')
            L_Spd, R_Spd = 0.8, 0.8
        elif label == 5:
            print('Stopping')
            R_Spd, L_Spd = 0.0, 0.0
        elif label == 6:
            print('Turning Right')
            if R_Spd >= 0:
                R_Spd = -R_Spd
            else: pass
            L_Spd = abs(L_Spd) # Left motor always positive to turn right
        elif label == 7:
            print('Turning Left')
            if L_Spd >= 0:
                L_Spd = -L_Spd
            else: pass
            R_Spd = abs(R_Spd) # Left motor always positive to turn right
        elif label == 8:
            print('Going Straight')
            R_Spd = abs(R_Spd)
            L_Spd = abs(L_Spd)

        move(L_Spd, R_Spd)
        sleep(time_stamp[i]/75) # Assuming its 45 fps

