import cv2
import numpy as np

class openCV():
    def __init__(self):
        '''
        Creates GUI
        '''
        clear = False

        # Create a black image (size:512*512)
        self.img = np.zeros((512, 512, 3), np.uint8)

        # Draw two digital blue lines
        cv2.line(self.img, (0, 256), (512, 256), (255, 0, 0), 2)
        cv2.line(self.img, (256, 0), (256, 512), (255, 0, 0), 2)

        if clear == False:
            # Show the result
            self.winName = 'Electronic Level'
            cv2.namedWindow(self.winName)
            cv2.imshow(self.winName, self.img)
            clear = True
            cv2.waitKey(0)
            cv2.destroyWindow(self.winName)

    def position(self, x, y):
        # Draw a filled yellow circle
        cv2.circle(self.img, (x, y), 25, (0, 255, 255), -1)
        cv2.imshow(self.winName, self.img)

