import sys
from mpu_module import mpu
from cv2_module import openCV

# Sends calibrated data and initialize camera
Mpu = mpu(-7.5634,20.5034,-34.7336,-6.7746)
OpenCV = openCV()

def main():
        OpenCV.Camera()
        [x ,y, angle] = Mpu.read_mpu()
        OpenCV.Elec_lvl(x, y)
        OpenCV.Elec_compass(angle)

        #imgStack = OpenCV.join(0.6,([compass,camera,level]))
        #cv2.imshow("Task 3", imgStack)
        #cv2.waitKey(1)

        #OpenCV.hor_stack(compass, camera, level)

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        OpenCV.close()
        sys.exit()