import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
from pathlib import Path

batch_size = 70
img_height = 32
img_width = 32

data_dir = Path('Traffic Data')

#SpdLimit30 = list(data_dir.glob('0/*'))

image_count = len(list(glob.glob('Datasets/*/*')))

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split = 0.2,
    subset = "training",
    seed = 123,
    image_size = (img_height, img_width),
    batch_size = batch_size
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split = 0.2,
    subset = "validation",
    seed = 123,
    image_size = (img_height, img_width),
    batch_size = batch_size
)

class_names = ['Speed Limit 30km/hr','Speed Limit 50km/hr','Speed Limit 70km/hr',
               'Speed Limit 80km/hr','Speed Limit 100km/hr', 'Stop', 'Turn Right Ahead',
               'Turn Left Ahead', 'Straight Ahead']
class_labels = train_ds.class_names

"""train_img, train_labels = [], []
for image_batch, labels_batch in train_ds:
    for i in range(len(image_batch)):
        train_img.append(image_batch)
        train_labels.append(labels_batch)"""

test_img, test_labels = [], []
for image_batch, labels_batch in val_ds:
    test_img = image_batch.numpy()
    test_labels = labels_batch.numpy()

test_img = test_img / 255.0

plt.figure(figsize=(10,10))
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_img[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[test_labels[i]])
plt.show()

"""train_img, train_labels = [], []
for images, labels in train_ds:
    for i in range(len(images)):
        train_img.append(images)
        train_labels.append(labels)

plt.figure(figsize = (10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
plt.show()"""



