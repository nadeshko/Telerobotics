import cv2
import numpy as np

def thresholding(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([0, 0, 0])
    upperWhite = np.array([179, 40, 255])
    maskWhite = cv2.inRange(imgHSV, lowerWhite, upperWhite)
    return maskWhite

def warping(img, points, w, h, inverse = False):
    pt1 = np.float32(points)
    pt2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    if inverse:
        matrix = cv2.getPerspectiveTransform(pt2, pt1)
    else:
        matrix = cv2.getPerspectiveTransform(pt1, pt2) # relates pt1 and pt2
    imgWarp = cv2.warpPerspective(img, matrix, (w,h))
    return imgWarp

def nothing(a):
    pass

def initializeTrackbars(intialTracbarVals, wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", intialTracbarVals[0],wT//2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", intialTracbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", intialTracbarVals[2],wT//2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", intialTracbarVals[3], hT, nothing)

def valTrackbars(wT = 480, hT = 240):
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT-widthTop, heightTop),
                      (widthBottom , heightBottom ), (wT-widthBottom, heightBottom)])
    return points

def drawPoints(img, points):
    for x in range(4):
        cv2.circle(img,(int(points[x][0]), int(points[x][1])), 10, (0,0,255), cv2.FILLED)
    return img

def getHistogram(img, minPer = 0.1, display = False, region = 1):
    if region == 1:
        histValues = np.sum(img, axis=0)
    else:
        histValues = np.sum(img[img.shape[0]//region:,:], axis=0)

    maxVal = np.max(histValues)
    minVal = minPer*maxVal # Accounts 10% of value as path, rest is noise

    indexArray = np.where(histValues >= minVal) #give a list of array for values greater than minimum values
    basePt = int(np.average(indexArray)) # Int so its plotable, not float

    if display: #DEBUG
        imgHist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        for x, intensity in enumerate(histValues):
            cv2.line(imgHist, (x, img.shape[0]), (x, img.shape[0]-intensity//255//region), (255, 0, 255), 1)
            cv2.circle(imgHist,(basePt, img.shape[0]), 20,  (0,255,255), cv2.FILLED) # ROBOT FACE
        return basePt, imgHist

    return basePt

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


