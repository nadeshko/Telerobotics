from _XiaoRGEEK_SERVO_ import XR_Servo

# Initializing Servo for robot arms
Servo = XR_Servo()

class Servo_control():
    def __init__(self, S1, S2, S3, S4):
        '''
        Servo Setup and initial angles
        '''
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3
        self.S4 = S4
        print("Starting Servo")

        # Initialize Servo Angle
        Servo.XiaoRGEEK_SetServoAngle(1, self.S1)
        Servo.XiaoRGEEK_SetServoAngle(2, self.S2)
        Servo.XiaoRGEEK_SetServoAngle(3, self.S3)
        Servo.XiaoRGEEK_SetServoAngle(4, self.S4)

#                (S1, S2,  S3,  S4)
#Basic(initial): (55, 90,  170, 90)
#Grab(step1)   : (10, 90,  125, 90)  *S3 should move first
#Grab(step2)   : (10, 90,  125, 180)
#Grab(step3)   : (55, 90,  170, 180) *S1 shoud move first
#Grab(step4)   : (55, 0,   170, 180)
#Grab(step5)   : (55, 90,  170, 180)
#Grab(step6)   : (10, 90,  125, 180) *S3 should move first
#Grab(step7)   : (10, 90,  125, 90)
#Back to basic

    def basic(self, servo):
        Servo.XiaoRGEEK_SetServoAngle(1, 55)
        Servo.XiaoRGEEK_SetServoAngle(2, 90)
        Servo.XiaoRGEEK_SetServoAngle(3, 170)
        Servo.XiaoRGEEK_SetServoAngle(4, 90)

    def grab1(self, servo):
        for i in range of (170, 125, -5):
         Servo.XiaoRGEEK_SetServoAngle(3, i)
        
        for i in range of (55, 10, -5):
         Servo.XiaoRGEEK_SetServoAngle(1, i)
        
        Servo.XiaoRGEEK_SetServoAngle(2, 90)
        Servo.XiaoRGEEK_SetServoAngle(4, 90)
        
    def grab2(self, servo):
        for i in range of (90, 180, 10):
         Servo.XiaoRGEEK_SetServoAngle(4, i)
        
        Servo.XiaoRGEEK_SetServoAngle(1, 10) 
        Servo.XiaoRGEEK_SetServoAngle(2, 90)
        Servo.XiaoRGEEK_SetServoAngle(3, 125)
        
        
    def grab3(self,servo):
        for i in range of (10, 55, 5):
         Servo.XiaoRGEEK_SetServoAngle(1, i)
        
        for i in range of (125, 170, 5):
         Servo.XiaoRGEEK_SetServoAngle(3, i)
        
        Servo.XiaoRGEEK_SetServoAngle(2, 90)
        Servo.XiaoRGEEK_SetServoAngle(4, 180)
        
    def grab4(self, servo):
        for i in range of (90, 0, -10):
         Servo.XiaoRGEEK_SetServoAngle(2, i)
         
        Servo.XiaoRGEEK_SetServoAngle(1, 55)
        Servo.XiaoRGEEK_SetServoAngle(3, 170)
        Servo.XiaoRGEEK_SetServoAngle(4, 180)
        
    def grab5(self, servo):
        for i in range of (0, 90, 10):
         Servo.XiaoRGEEK_SetServoAngle(2, i)
         
        Servo.XiaoRGEEK_SetServoAngle(1, 55)
        Servo.XiaoRGEEK_SetServoAngle(3, 170)
        Servo.XiaoRGEEK_SetServoAngle(4, 180)
        
    def grab6(self, servo):
        for i in range of (170, 125, -5):
         Servo.XiaoRGEEK_SetServoAngle(3, i)
         
        for i in range of (55, 10, -5):
         Servo.XiaoRGEEK_SetServoAngle(1, i)
        
        Servo.XiaoRGEEK_SetServoAngle(2, 90)
        Servo.XiaoRGEEK_SetServoAngle(4, 180)
        
    def grab7(self, servo):
        for i in range of (180, 90 , -10):
         Servo.XiaoRGEEK_SetServoAngle(4, i)
        
        Servo.XiaoRGEEK_SetServoAngle(1, 10)
        Servo.XiaoRGEEK_SetServoAngle(2, 90)
        Servo.XiaoRGEEK_SetServoAngle(3, 125)
        

  

def main():
    basic()
    time.sleep(1)
    grab1()
    time.sleep(1)
    grab2()
    time.sleep(1)
    grab3()
    time.sleep(1)
    grab4()
    time.sleep(1)
    grab5()
    time.sleep(1)
    grab6()
    time.sleep(1)
    grab7()
    time.sleep(1)
    basic()
    
if __name__ == '__main__':
    servo = Servo(10, 90, 125, 90)
    while True:
        main()            