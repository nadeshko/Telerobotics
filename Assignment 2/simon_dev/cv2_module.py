import cv2
import imutils
import numpy as np

class openCV():
    def __init__(self):
        '''
        Initialize Camera
        '''
        self.cap = cv2.VideoCapture(0)
        "Starting Camera"

    def Camera(self):
        success, frame = self.cap.read()
        cv2.imshow('Camera', frame)
        k = cv2.waitKey(1) % 256
        if k == 27:  # ESC
            print("quitting...")
            cv2.destroyAllWindows()
        
    def Elec_lvl(self, x, y):
        # Create a black image (size:512*512)
        img = np.zeros((512, 512, 3), np.uint8)
        # Draw two digital blue lines
        cv2.line(img, (0, 256), (512, 256), (255, 0, 0), 1)
        cv2.line(img, (256, 0), (256, 512), (255, 0, 0), 1)
        # Draw a filled cycle
        cv2.circle(img, (x, y), 28, (0, 255, 255), -1)
        # Show the result
        cv2.imshow('Electronic Level', img)
        cv2.namedWindow('Electronic Level')
        cv2.waitKey(250)

    def Elec_compass(self, angle):
        # Load image from file
        compass= cv2.imread("compass4.png")
        rotating = imutils.rotate(compass, -angle)
        cv2.imshow("Electronic Compass", rotating)
        cv2.waitKey(250)

    def close(self):
        '''
        Closes the camera and destroys all window
        '''
        self.cam.release()
        cv2.destroyAllWindows()










