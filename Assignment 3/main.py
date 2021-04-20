import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from skimage import color
from pathlib import Path

def plot():
    # color map for grayscale pictures
    plt.figure()
    plt.imshow(train_img[453])
    plt.colorbar()
    plt.grid(False)

    # display training set images for confirmation
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_img[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()

# Initial Parameters
num_classes = 9
batch_size = 12000
img_height = 32
img_width = 32

class_names = ['Speed Limit 30km/hr','Speed Limit 50km/hr','Speed Limit 70km/hr',
               'Speed Limit 80km/hr','Speed Limit 100km/hr', 'Stop', 'Turn Right Ahead',
               'Turn Left Ahead', 'Straight Ahead']

data_dir = Path('Traffic Data')

#images = np.asarray(list(data_dir.glob('*/*')))
#labels = list(map(int, (os.listdir(data_dir))))
#print(images.shape)

# Importing images and labels into dataset
dataset = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    seed = 123,
    image_size = (img_height, img_width),
    batch_size = batch_size)

# moving images & labels to n-dimension array
images, labels = [], []
for image_batch, labels_batch in dataset:
    images = image_batch.numpy().astype("uint8")
    labels = labels_batch.numpy()
    break

# Convert images to grayscale and normalizing to [0,1]
images = color.rgb2gray(images)
images = images / 255.0

# Splitting data into training(0.8) and test(0.2) data's
train_img, test_img, train_labels, test_labels = train_test_split(images, labels, test_size = 0.2)
#plot() # DEBUG

### Building the Sequential Model
# Setting up layers
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape = (32, 32)), # Tranforms format of images from 2D -> 1D array
    tf.keras.Dense(128, activation='relu'), # 128 nodes
    tf.keras.Dense(num_classes)]) # last layer
# Compiling Model
model.compile(
    optimizer = 'adam',
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
    metrics = ['accuracy'])
# Model Summary
model.summary()








