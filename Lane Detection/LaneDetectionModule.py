import cv2
import utlis
import numpy as np

curveList = []
AvgVal = 10

def getLane(img, display = 2):

    imgCopy = img.copy()
    imgResult = img.copy()

    ### STEP 1:
    imgThres = utlis.thresholding(img) # Sending image and getting it back

    ### STEP 2:
    hT, wT, c = img.shape # using trackbars to get points
    points = utlis.valTrackbars()
    imgWarp = utlis.warping(imgThres, points, wT, hT)
    imgWarpPoint = utlis.drawPoints(imgCopy, points)

    ### STEP 3:
    midPt, imgHist = utlis.getHistogram(imgWarp, minPer=0.5, display=True, region=4)
    curveAvgPt, imgHist = utlis.getHistogram(imgWarp, minPer=0.9, display=True, region=1)
    curveRaw = curveAvgPt - midPt

    ### STEP 4:
    curveList.append(curveRaw)
    if len(curveList) > AvgVal:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))

    ### STEP 5:
    if display != 0:
        imgInvWarp = utlis.warping(imgWarp, points, wT, hT, inverse=True)
        imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
        imgInvWarp[0:hT // 3, 0:wT] = 0, 0, 0
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 255, 0
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
        midY = 450
        cv2.putText(imgResult, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
        cv2.line(imgResult, (wT // 2, midY), (wT // 2 + (curve * 3), midY), (255, 0, 255), 5)
        cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY - 25), (wT // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
        for x in range(-30, 30):
            w = wT // 20
            cv2.line(imgResult, (w * x + int(curve // 50), midY - 10),
                     (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)
        #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        #cv2.putText(imgResult, 'FPS ' + str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230, 50, 50), 3);
    if display == 2:
        imgStacked = utlis.stackImages(0.7, ([img, imgWarpPoint, imgWarp],
                                             [imgHist, imgLaneColor, imgResult]))
        cv2.imshow('ImageStack', imgStacked)
    elif display == 1:
        cv2.imshow('Result', imgResult)

    return curve

def main():
    success, img = cap.read()
    fin = cv2.resize(img, (480, 240))
    curve = getLane(fin, display=2)
    print(curve)
    cv2.waitKey(35)

if __name__ == '__main__':
    frameCounter = 0
    cap = cv2.VideoCapture('Lane.mp4')
    initialTBvals = [51, 164, 28, 216]
    utlis.initializeTrackbars(initialTBvals)
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
        main()
        