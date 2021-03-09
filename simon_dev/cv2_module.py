import cv2
import numpy as np

class openCV():
    def __init__(self):
        # Create a black image (size:512*512)
        self.img = np.zeros((512, 512, 3), np.uint8)
        # Draw two digital blue lines
        cv2.line(self.img, (0, 256), (512, 256), (255, 0, 0), 1)
        cv2.line(self.img, (256, 0), (256, 512), (255, 0, 0), 1)
        # Show the result
        self.winName = 'Electronic Level'
        cv2.namedWindow(self.winName)

    def Update(self, x, y):
        # Draw a filled cycle
        cv2.circle(self.img, (x,y), 28, (0, 255, 255), -1)
        cv2.imshow(self.winName, self.img)
        cv2.waitKey(500)






