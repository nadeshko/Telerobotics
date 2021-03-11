import cv2
import imutils
import argparse
import numpy as np

class openCV():
    def __init__(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--image", required=True, help="path to the image file")
        self.args = vars(ap.parse_args())

    def Elec_lvl(self, x, y):
        # Create a black image (size:512*512)
        self.img = np.zeros((512, 512, 3), np.uint8)
        # Draw two digital blue lines
        cv2.line(self.img, (0, 256), (512, 256), (255, 0, 0), 1)
        cv2.line(self.img, (256, 0), (256, 512), (255, 0, 0), 1)
        # Draw a filled cycle
        cv2.circle(self.img, (x, y), 28, (0, 255, 255), -1)
        # Show the result
        self.winName = 'Electronic Level'
        cv2.imshow(self.winName, self.img)
        cv2.namedWindow(self.winName)

        cv2.waitKey(250)

    def Elec_compass(self, angle):
        # Load image from file
        img = cv2.imread(self.args["Compass.png"])
        rotated = imutils.rotate_bound(img, angle)
        cv2.imshow("Electronic Compass", rotated)
        cv2.waitKey(0)










