import cv2
import numpy as np

# Create a black image (size:512*512)
img = np.zeros((512,512,3),np.uint8)

# Draw a digital blue (BGR:(255,0,0)) line from (0,0) to (511,511) on the black image with thickness of 5px
cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Draw a rectangle (Green,thickness:3 px)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw a filled cycle (red, radius:63)
cv2.circle(img,(447,63),63,(0,0,255),-1)

# Insert white text "OpenCV"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2)

# Show the result
winName = 'example'
cv2.namedWindow(winName)
cv2.imshow(winName,img)
cv2.waitKey(0)
cv2.destroyWindow(winName)