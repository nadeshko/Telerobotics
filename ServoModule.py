from _XiaoRGEEK_SERVO_ import XR_Servo

###########################################################################
###                             SERVO MODULE                            ###
###########################################################################

# Initializing Servo for robot arms
Servo = XR_Servo()

class Servo_control():
    def __init__(self, S1, S2, S3, S4, S7, S8):
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3
        self.S4 = S4
        self.S7 = S7
        self.S8 = S8
        print("Starting Servo")

        # Initialize Servo Angle
        Servo.XiaoRGEEK_SetServoAngle(1, self.S1)
        Servo.XiaoRGEEK_SetServoAngle(2, self.S2)
        Servo.XiaoRGEEK_SetServoAngle(3, self.S3)
        Servo.XiaoRGEEK_SetServoAngle(4, self.S4)
        Servo.XiaoRGEEK_SetServoAngle(7, self.S7)
        Servo.XiaoRGEEK_SetServoAngle(8, self.S8)

    def down(self, servo):
        if servo == 1:
            if self.S1 <= 0:
                self.S1 = 0
            else:
                self.S1 -= 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S1)
        elif servo == 2:
            if self.S2 <= 0:
                self.S2 = 0
            else:
                self.S2 -= 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S2)
        elif servo == 3:
            if self.S3 <= 0:
                self.S3 = 0
            else:
                self.S3 -= 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S3)
        elif servo == 4:
            if self.S4 <= 0:
                self.S4 = 0
            else:
                self.S4 -= 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S4)
        elif servo == 7:
            if self.S7 <= 0:
                self.S7 = 0
            else:
                self.S7 -= 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S7)
        elif servo == 8:
            if self.S8 <= 0:
                self.S8 = 0
            else:
                self.S8 -= 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S8)

    def up(self, servo):
        if servo == 1:
            if self.S1 >= 180:
                self.S1 = 180
            else:
                self.S1 += 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S1)
        elif servo == 2:
            if self.S2 >= 180:
                self.S2 = 180
            else:
                self.S2 += 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S2)
        elif servo == 3:
            if self.S3 >= 180:
                self.S3 = 180
            else:
                self.S3 += 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S3)
        elif servo == 4:
            if self.S4 >= 90:
                self.S4 = 90
            else:
                self.S4 += 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S4)
        elif servo == 7:
            if self.S7 >= 90:
                self.S7 = 90
            else:
                self.S7 += 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S7)
        elif servo == 8:
            if self.S8 >= 90:
                self.S8 = 90
            else:
                self.S8 += 5
            Servo.XiaoRGEEK_SetServoAngle(servo, self.S8)

def main():
    pass

if __name__ == '__main__':
    servo = Servo(0, 120, 90, 0, 0, 90)
    while True:
        main()