import RPi.GPIO as GPIO
from time import sleep
import pygame, os, time
import numpy as np
import cv2
from _XiaoRGEEK_SERVO_ import XR_Servo

screen = pygame.display.set_mode([500,300])

# Set GPIO call mode as BCM
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Allow Camera
cam = cv2.VideoCapture(0)

# Initializing Servo for robot arms
Servo = XR_Servo()

# Initial Values
Speed = 0
S7_Angle = 90
S8_Angle = 90
img_counter = 0
img = 0
x = 0
y = 0
angle = 0
Servo.XiaoRGEEK_SetServoAngle(7,S7_Angle)
Servo.XiaoRGEEK_SetServoAngle(8,S8_Angle)

if __name__ == '__main__':
    while True:
        ret, frame = cam.read()
        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)

        if k % 256 == 27:  # ESC
            print("Closing...")
            break
        elif k % 256 == 32:  # Space
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!\nPress g to grayscale, rotate and resize image!".format(img_name))
            img_counter += 1
        elif k % 256 == ord('g'):  # Change to grayscale
            # Reading Image
            img = input("which picture would you like to make grayscale?")
            gray_image = cv2.imread("opencv_frame_{}.png".format(img), 0)
            print("Changing opencv_frame_{}.png to grayscale!".format(img))
            # cv2.imshow("Grayscale Image", gray_image) # Debug

            y = int(input("what height would you want for the image?"))
            x = int(input("what length would you want for the image?"))
            print("resizing image to [{},{}]".format(x,y))
            numpy_image = np.asarray(gray_image)
            resize_image = cv2.resize(numpy_image, (x, y))

            #rotation = input("Turning clockwise, how much degree do you want it to turn? (90, 180, 270)")
            #print("rotating image by {} clockwise".format(rotation))
            #tetha = getattr(cv2, "ROTATE_{}_CLOCKWISE".format(rotation))
            rotate_image = cv2.rotate(resize_image,cv2.ROTATE_90_CLOCKWISE)
            cv2.imshow("Edited Image", rotate_image)


        #elif k % 256 == ord('s'):
            #numpy_image = np.asarray(gray_image)
            #resize_image = cv2.resize(numpy_image, (100,70))
            #print("Resizing {} to 1000,600!".format(img_name))
            #cv2.imshow("Resized Image", resize_image)
        elif k % 256 == ord('x'):  # Change to grayscale
            cv2.destroyAllWindows()

cam.release()
cv2.destroyAllWindows()