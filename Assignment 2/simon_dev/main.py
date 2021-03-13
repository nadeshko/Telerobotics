import sys
import cv2
from mpu_module import mpu
from cv2_module import openCV

# Sends calibrated data and initialize camera
Mpu = mpu(-7.5634,20.5034,-34.7336,-6.7746)
OpenCV = openCV()
cam = cv2.VideoCapture(1)

def main():
        ret, frame = cam.read()
        cv2.imshow('Camera', frame)

        #OpenCV.Camera()
        [x ,y, angle] = Mpu.read_mpu()
        OpenCV.Elec_lvl(x, y)
        OpenCV.Elec_compass(angle)
        cv2.waitKey(1)

        #imgStack = OpenCV.join(0.6,([compass,camera,level]))
        #cv2.imshow("Task 3", imgStack)
        #cv2.waitKey(1)

        #OpenCV.hor_stack(compass, camera, level)

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        cam.release()
        cv2.destroyAllWindows()
        sys.exit()