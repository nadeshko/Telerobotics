import cv2

## Capture the default camera
cap= cv2.VideoCapture(0)

while True::
     ## Caputure frame = cap.read()
     ret, frame = cap.read()
     
     ## Display the resulting frame
     cv2.imshow('frame',frame)
     
     ## Wait for 'q' to break the loop
     if cv2.waitKey(1)&0xFF == ord('q'):
      break
     
## Release the capture
cap.release()
cv2.destroyAllWindows()