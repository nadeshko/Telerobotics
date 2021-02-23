import cv2

## Load the image
## If the the image to be read in is not in the same directory as the code, file, writting the full path is required

img = cv2.imshow('image',img)

## Check keyboard input
input_key = cv2.waitKey(0)&0xFF
# Wait for 'esc' to exit
if input_key == 27:
           cv2.imwrite("Duplicate_image",img)
# Wait for 's' to save the image before exit
elif input_key == ord('s'):
           cv2.imwrite("Duplicate_image",img)
           cv2.destroyAllWindows()

