import cv2
import utlis
import numpy as np

if __name__ == '__main__':
    cap = cv2.VideoCapture('cam.mp4')
    while True:
        success, img = cap.read()
        #fin = cv2.resize(img,(480,240))
        cv2.imshow('Video',img)
        cv2.waitKey(10)