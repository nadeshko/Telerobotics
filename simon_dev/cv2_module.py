import cv2
import numpy as np

class openCV():
    def __init__(self, x, y): # <- what do you want x and y from accel for?
        # Create a black image (size:512*512)
        img = np.zeros((512, 512, 3), np.uint8)

        # Draw a filled cycle
        cv2.circle(img, (x,y), 28, (0, 255, 255), -1)

        # Draw two digital blue lines
        cv2.line(img, (0, 256), (512, 256), (255, 0, 0), 1)
        cv2.line(img, (256, 0), (256, 512), (255, 0, 0), 1)

        # Show the result
        winName = 'Electronic Level'
        cv2.namedWindow(winName)
        cv2.imshow(winName, img)
        cv2.waitKey(0)
        cv2.destroyWindow(winName)

