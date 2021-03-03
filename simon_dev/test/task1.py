# developing
import cv2
import numpy as np

# Create a black image (size:512*512)
img = np.zeros((512,512,3),np.uint8)

# Draw a rectangle (Green,thickness:3 px)
# cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw a filled cycle (red, radius:63)
# cv2.circle(imgage, centre(x,y), radius, color(,,), thickness)
# thickness (-1) ti filled the cycle 
cv2.circle(img,(256,256),28,(0,255,255),-1)

# Draw a digital blue (BGR:(255,0,0)) line from (0,0) to
# (511,511) on the black image with thickness of 5px
# cv2.line(imgae, start(x,y), end(x,y), color(B,G,R), thickness)
cv2.line(img,(0,256),(512,256),(255,0,0),1)
cv2.line(img,(256,0),(256,512),(255,0,0),1)

# Insert white text "OpenCV"
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2)

# Show the result
winName = 'Electronic Level'
cv2.namedWindow(winName)
cv2.imshow(winName,img)
cv2.waitKey(0)
cv2.destroyWindow(winName)