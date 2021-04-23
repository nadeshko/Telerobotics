from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.layers.experimental import preprocessing
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential, layers
from skimage import color
from pathlib import Path
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

def plot_graph():
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.xlabel('Epoch')
    plt.title('Training and Validation Accuracy')

    plt.subplot(2, 1, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.xlabel('Epoch')
    plt.title('Training and Validation Loss')

def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    predicted_label = np.argmax(predictions_array)

    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)

    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    plt.xlabel(f"{class_names[predicted_label]} {(100*np.max(predictions_array)):2.0f}% ({class_names[true_label]})",
               color=color)

def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    predicted_label = np.argmax(predictions_array)

    plt.grid(False)
    plt.xticks(range(9))
    plt.yticks([])
    plt.ylim([0, 1])
    this_plot = plt.bar(range(9), predictions_array, color="#777777")
    this_plot[predicted_label].set_color('red')
    this_plot[true_label].set_color('blue')

# Initial Parameters
num_classes = 9
num_images = 11429
img_height = 32
img_width = 32
batch_size = 100

train_ratio = 0.75
validation_ratio = 0.15
test_ratio = 0.1

class_names = ['30km/hr','50km/hr','70km/hr', '80km/hr','100km/hr', 'Stop', 'Turn Right',
               'Turn Left', 'Straight']

data_dir = Path('Traffic Data')

# Importing images and labels into dataset
dataset = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    seed = 123,
    image_size = (img_height, img_width),
    batch_size = num_images)

# moving images & labels to n-dimension array
images, labels = [], []
for image_batch, labels_batch in dataset:
    images = image_batch.numpy().astype("uint8")
    labels = labels_batch.numpy()
    break

# Convert images to grayscale and normalizing to [0,1]
images = images / 255.0

# Splitting data into training(0.75), validation(0.15), and test(0.1) data sets
train_img, test_img, train_labels, test_labels = train_test_split(
    images, labels, test_size = 1 - train_ratio)
val_img, test_img, val_labels, test_labels = train_test_split(
    test_img, test_labels, test_size = test_ratio / (test_ratio + validation_ratio))