from keras import models
from PIL import Image
import numpy as np
import cv2

# Load saved model
model = models.load_model('CNN_model') # input: 1x32x32x3
video = cv2.VideoCapture(0)

while True:
    _, frame = video.read()

    # convert captures from into RGB
    im = Image.fromarray(frame, 'RGB')

    # Resizing into 32x32
    im = im.resize((128,128))
    img_array = np.array(im)

    img_array = np.expand_dims(img_array, 0)

    # Predicting image using model
    prediction = int(model.predict(img_array)[0][0])

    # if prediction is 0, which means img is missing, frame = gray color.
    if prediction == 0:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Capturing', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

if __name__ == '__main__':
    frameCounter = 0
    cap = cv2.VideoCapture('LowRes.mp4')
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
        main()
