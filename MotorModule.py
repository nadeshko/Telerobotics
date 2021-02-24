import RPi.GPIO as GPIO

###########################################################################
###                            Motor Module                             ###
###########################################################################

# Set GPIO call mode as BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor_Control():
    def __init__(self, ENA, ENB, IN1, IN2, IN3, IN4):
        self.ENA = ENA
        self.ENB = ENB
        self.IN1 = IN1
        self.IN2 = IN2
        self.IN3 = IN3
        self.IN4 = IN4
        print("Starting Robot")

        # Port Setup
        GPIO.setup(self.ENA, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.ENB, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.IN4, GPIO.OUT, initial=GPIO.LOW)

        # Specify the PWM control port and the frequency of the PWM signal
        self.RightM = GPIO.PWM(self.ENA, 1000)
        self.LeftM = GPIO.PWM(self.ENB, 1000)

        # Start PWM
        self.RightM.start(0)
        self.LeftM.start(0)

    # Movement functions
    def Forward(self, Speed):
        Speed *= 100
        self.RightM.ChangeDutyCycle(Speed)
        self.LeftM.ChangeDutyCycle(Speed)
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, True)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, True)

    def Backward(self, Speed):
        Speed *= 100
        self.RightM.ChangeDutyCycle(Speed)
        self.LeftM.ChangeDutyCycle(Speed)
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, True)
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, True)
        GPIO.output(self.IN4, False)

    def Right(self, Speed):
        Speed *= 100
        self.RightM.ChangeDutyCycle(Speed)
        self.LeftM.ChangeDutyCycle(Speed)
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, True)
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, True)

    def Left(self, Speed):
        Speed *= 100
        self.RightM.ChangeDutyCycle(Speed)
        self.LeftM.ChangeDutyCycle(Speed)
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, True)
        GPIO.output(self.IN3, True)
        GPIO.output(self.IN4, False)

    # Stop function
    def Stop(self):
        self.RightM.ChangeDutyCycle(0)
        self.LeftM.ChangeDutyCycle(0)
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, False)

def main():
    pass

if __name__ == '__main__':
    motor1 = Motor(13, 20, 19, 16, 21, 26)
    while True:
        main()


