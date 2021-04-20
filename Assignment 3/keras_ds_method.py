import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from skimage import color
from pathlib import Path

batch_size = 32
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
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split = 0.2,
    subset = "training",
    seed = 123,
    image_size = (img_height, img_width),
    batch_size = batch_size)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split = 0.2,
    subset = "validation",
    seed = 123,
    image_size = (img_height, img_width),
    batch_size = batch_size)

# moving images N labels to ndarray
images, labels = [], []
for image_batch, labels_batch in train_ds:
    images = image_batch.numpy().astype("uint8")
    labels = labels_batch.numpy()
    break
# Convert images to grayscale
images = color.rgb2gray(images)

# Splitting datasets
train_test_split


images = images / 255.0

plt.figure()
plt.imshow(images[3477])
plt.colorbar()
plt.grid(False)

plt.figure(figsize = (10, 10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(images[i], cmap = plt.cm.binary)
    plt.xlabel(class_names[labels[i]])
plt.show()









