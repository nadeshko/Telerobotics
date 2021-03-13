import cv2
import imutils
import argparse
import numpy as np
from PIL import Image

class openCV():
    def __init__(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--image", help="path to the image file")
        args = vars(ap.parse_args())
        # Load image from file
        self.compass= cv2.imread("compass4.png")
        #pass
        
    def Elec_lvl(self, x, y):
        # Create a black image (size:512*512)
        img = np.zeros((512, 512, 3), np.uint8)
        # Draw two digital blue lines
        cv2.line(img, (0, 256), (512, 256), (255, 0, 0), 1)
        cv2.line(img, (256, 0), (256, 512), (255, 0, 0), 1)
        # Draw a filled cycle
        cv2.circle(img, (x, y), 28, (0, 255, 255), -1)
        # Show the result
        winName = 'Electronic Level'
        cv2.imshow(winName, img)
        cv2.namedWindow(winName)

        cv2.waitKey(250)

    def Elec_compass(self, angle):
        # Load image from file
        #img = cv2.imread(self.args["compass1.png"])

        # Grab the dimension of the image and calculate the centre of the image
        #(h, w) = image.shape[:2]
        #(cX, cY) = (w//2, h//2)

        # Rotate the image with boundaries
        
        self.compass= cv2.imread("compass4.png")
        angle_alt = -angle
        rotated = imutils.rotate(self.compass, angle_alt)
        cv2.imshow("Electronic Compass", rotated)
        cv2.waitKey(50)
        # # Create an Image object from an Image
        # colorImage = Image.open("compass4.png")
        # # Rotate it by 45 degrees
        # rotated = colorImage.rotate(-angle)
        # # Display the Image and rotate along with the angle
        # rotated.show()









