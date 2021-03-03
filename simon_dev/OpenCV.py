# developing
import cv2
import numpy as np


def OpenCV(x,y):

 # Create a black image (size:512*512)
 img = np.zeros((512,512,3),np.uint8)

 # Draw a filled cycle
 cv2.circle(img,(x,y),28,(0,255,255),-1)

# Draw two digital blue lines
 cv2.line(img,(0,256),(512,256),(255,0,0),1)
 cv2.line(img,(256,0),(256,512),(255,0,0),1)
 
 # Show the result
 winName = 'Electronic Level'
 cv2.namedWindow(winName)
 cv2.imshow(winName,img)
 cv2.waitKey(0)
 cv2.destroyWindow(winName)
 
if __name__ == '__main__':
    while True:
        close = OpenCV(256,256)
        if close == False:
            break