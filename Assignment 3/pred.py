from keras import models
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

class_names = ['30km/hr', '50km/hr', '70km/hr', '80km/hr', '100km/hr', 'Stop', 'Turn Right',
                'Turn Left', 'Straight']
desired_size = 32
frameCounter = 0 # DEBUG

# Load saved model

model = models.load_model('saved_model/CNN_model') # input: 1x32x32x3
video = cv2.VideoCapture('LowRes.mp4')

while True:
    frameCounter += 1
    if video.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0

    _, frame = video.read()

    size = frame.shape
    border = int((size[1]-size[0])/2)
    im = cv2.copyMakeBorder(frame, border, border, 0, 0, cv2.BORDER_CONSTANT)

    # convert captures into RGB
    im = Image.fromarray(im, 'RGB')

    # Resizing into 32x32
    im = im.resize((32, 32))
    img_array = np.array(im)

    img_array = np.expand_dims(img_array, 0)

    # Predicting image using model
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = round(100*np.max(prediction), 2)

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, f'{confidence}% {predicted_class}',
                (int(size[1]-size[1]*0.4), int(size[0]-size[0]*0.1)),
                font, 1.5, (0, 0, 255), 2, cv2.LINE_4)
    cv2.imshow('Prediction', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()