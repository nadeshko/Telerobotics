import cv2
import numpy as np

###########################################################################
###                            CAMERA MODULE                            ###
###########################################################################

class Camera():
    def __init__(self):
        self.img_counter = 0
        self.out = False

        # Allow Camera
        self.cam = cv2.VideoCapture(0)
        print("Starting Camera")

    def open(self):
        '''
        Shows camera window and allows user key input
        '''
        ret, frame = self.cam.read()
        cv2.imshow('Camera', frame)