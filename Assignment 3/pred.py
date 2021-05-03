from keras import models
from PIL import Image
import pandas as pd
import numpy as np
import cv2

def get_majority(list_range, default=None):
    """Find which element in *seq* sequence is in the majority.

    Return *default* if no such element exists.

    Use Moore's linear time constant space majority vote algorithm
    """
    candidate = default
    count = 0
    for e in list_range:
        if count != 0:
            count += 1 if candidate == e else -1
        else: # count == 0
            candidate = e
            count = 1

    # check the majority
    return candidate if list_range.count(candidate) >= len(list_range) // 2 else candidate

file_path = 'robot_control.csv'

class_names = ['30km/hr', '50km/hr', '70km/hr', '80km/hr', '100km/hr', 'Stop', 'Turn Right',
                'Turn Left', 'Straight']
desired_size = 32
frameCounter = 0
timeCounter = 0

# Load saved model + video
model = models.load_model('saved_model/CNN_model') # input: 1x32x32x3
video = cv2.VideoCapture('test2.mp4')

class_labels = []
class_list, time_stamp = [], []

while True:
    frameCounter += 1
    if video.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter: # Debug
        array = np.column_stack((class_list, time_stamp))
        df = pd.DataFrame(array)
        df.to_csv(file_path, index=False)
        break

    _, frame = video.read()

    # Get video size and keep aspect ratio
    size = frame.shape
    border = int((size[1]-size[0])/2)
    im = cv2.copyMakeBorder(frame, border, border, 0, 0, cv2.BORDER_CONSTANT)

    # Convert captures into RGB
    im = Image.fromarray(im, 'RGB')

    # Resizing and reshaping video
    im = im.resize((32, 32))
    img_array = np.array(im)
    img_array = np.expand_dims(img_array, 0)

    # Predicting image using model
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = round(100*np.max(prediction), 2)

    # Show text while video is playing
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, f'{confidence}% {predicted_class}',
                (int(size[1]-size[1]*0.4), int(size[0]-size[0]*0.1)),
                font, 1.5, (255, 0, 0), 2, cv2.LINE_4)
    cv2.imshow('Prediction', frame)

    class_labels.append(np.argmax(prediction))
    # Ignoring random and uncertain values
    class_list.append(get_majority(class_labels[frameCounter-23:frameCounter]))
    timeCounter += 1
    if frameCounter > 1:
        if class_list[frameCounter-1] != class_list[frameCounter-2]:
           timeCounter = 0
    time_stamp.append(timeCounter)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()