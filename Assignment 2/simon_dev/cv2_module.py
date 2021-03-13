import cv2
import imutils
import numpy as np

class openCV():
    def __init__(self):
        '''
        Initialize Camera
        '''
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 640)
        self.cam.set(4, 480)

    def Camera(self):
        ret, frame = self.cam.read()
        #return frame
        cv2.imshow('Camera', frame)
        cv2.waitKey(1)
        
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
        #return img

    def Elec_compass(self, angle):
        # Load image from file
        self.compass= cv2.imread("compass4.png")
        resize = cv2.resize(self.compass, (512,512))
        rotating = imutils.rotate(resize, -angle)
        cv2.imshow("Electronic Compass", rotating)
        cv2.waitKey(250)
        #return rotating

    def hor_stack(self, img1, img2, img3):
        horImg = np.hstack((img1, img2, img3))
        cv2.imshow("Horizontal", horImg)
        cv2.waitKey(1)

    def join(self, scale, imgArray):
        rows = len(imgArray)
        cols = len(imgArray[0])
        rowsAvailable = isinstance(imgArray[0], list)
        width = imgArray[0][0].shape[1]
        height = imgArray[0][0].shape[0]
        if rowsAvailable:
            for x in range(0, rows):
                for y in range(0, cols):
                    if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                        imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                    else:
                        imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                    None, scale, scale)
                    if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
            imageBlank = np.zeros((height, width, 3), np.uint8)
            hor = [imageBlank] * rows
            hor_con = [imageBlank] * rows
            for x in range(0, rows):
                hor[x] = np.hstack(imgArray[x])
            ver = np.vstack(hor)
        else:
            for x in range(0, rows):
                if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                    imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
                else:
                    imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale,
                                             scale)
                if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
            hor = np.hstack(imgArray)
            ver = hor
        return ver

    def close(self):
        '''
        Closes the camera and destroys all window
        '''
        self.cam.release()
        cv2.destroyAllWindows()










