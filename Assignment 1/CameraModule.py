import cv2
import numpy as np

###########################################################################
###                            CAMERA MODULE                            ###
###########################################################################

class Camera():
    def __init__(self):
        self.img_counter = 0
        self.out = False

        # Allow Camera
        self.cam = cv2.VideoCapture(0)
        print("Starting Camera")

    def open(self):
        '''
        Shows camera window and allows user key input
        '''
        ret, frame = self.cam.read()
        cv2.imshow('Camera', frame)

        k = cv2.waitKey(1)

        if k % 256 == 27:  # ESC
            print("Closing...")
            self.out = True
            #self.cam.release()
            #cv2.destroyAllWindows()
        elif k % 256 == 32:  # Space
            img_name = "opencv_frame_{}.png".format(self.img_counter)
            cv2.imwrite(img_name, frame)
            print(f"{img_name} written!\nPress g to grayscale, resize and rotate a written image!")
            self.img_counter += 1
        elif k % 256 == ord('g'):  # Editing a chosen image
            # Reading Image and converting to grayscale
            img = input("In integer, which picture would you like to make grayscale?")
            gray_image = cv2.imread(f"opencv_frame_{img}.png", 0)
            print(f"Changing opencv_frame_{img}.png to grayscale!")
            # Input Image size to resize to
            y = int(input("How tall?"))
            x = int(input("How long horizontally?"))
            print(f"resizing image to [{x},{y}]")
            numpy_image = np.asarray(gray_image)
            resize_image = cv2.resize(numpy_image, (x, y))
            # Rotate image 90 degrees and show
            rotate_image = cv2.rotate(resize_image, cv2.ROTATE_90_CLOCKWISE)
            cv2.imshow("Edited Image", rotate_image)

        elif k % 256 == ord('x'):  # Change to grayscale
            cv2.destroyAllWindows()

        return self.out

    def close(self):
        '''
        Closes the camera and destroys all window
        '''
        self.cam.release()
        cv2.destroyAllWindows()