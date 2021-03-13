import cv2
from utlis import utilities
import numpy as np

cap = cv2.VideoCapture('Lane.mp4')

def getLane(img):
    imgThres = utilities.thresholding(img) # Sending image and getting it back
    cv2.imshow('Threshold',imgThres)
    return None

def main():
    success, img = cap.read()
    fin = cv2.resize(img, (480, 240))
    getLane(fin)
    cv2.imshow('Video', fin)
    cv2.waitKey(35)

if __name__ == '__main__':
    while True:
        main()
        