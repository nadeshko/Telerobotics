import cv2
import imutils
import numpy as np

class openCV():
    def __init__(self):
        '''
        Initialize Camera
        '''
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)
        print("Starting Camera")

    def Camera(self):
        success, frame = self.cap.read()
        cv2.imshow('Camera', frame)
        cv2.waitKey(1)
        
    def Elec_lvl(self, x, y):
        # Create a black image (size:512*512)
        img = np.zeros((480, 480, 3), np.uint8)
        # Draw two digital blue lines
        cv2.line(img, (0, 240), (480, 240), (255, 0, 0), 1)
        cv2.line(img, (240, 0), (240, 480), (255, 0, 0), 1)
        # Draw a filled cycle
        cv2.circle(img, (x, y), 22, (0, 255, 255), -1)
        # Show the result
        cv2.imshow('Electronic Level', img)
        cv2.namedWindow('Electronic Level')
        cv2.waitKey(250)

    def Elec_compass(self, angle):
        # Load image from file
        compass = cv2.imread("compass.png")
        resize = cv2.resize(compass, (480,480))
        rotating = imutils.rotate(resize, -angle)
        cv2.imshow("Electronic Compass", rotating)
        cv2.waitKey(250)

    def close(self):
        '''
        Closes the camera and destroys all window
        '''
        self.cap.release()
        cv2.destroyAllWindows()










