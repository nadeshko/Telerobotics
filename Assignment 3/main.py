from tensorflow.keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
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
    plt.title('Training and Validation Accuracy')

    plt.subplot(2, 1, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
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
batch_size = 200

class_names = ['30km/hr','50km/hr','70km/hr', '80km/hr','100km/hr', 'Stop', 'Turn Right',
               'Turn Left', 'Straight']

data_dir = Path('Traffic Data')

# Importing images and labels into dataset
dataset = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    seed = 124,
    image_size = (img_height, img_width),
    batch_size = num_images)

# moving images & labels to n-dimension array
images, labels = [], []
for image_batch, labels_batch in dataset:
    images = image_batch.numpy().astype("uint8")
    labels = labels_batch.numpy()
    break
"""
datagen = ImageDataGenerator(
    rotation_range = 40,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    fill_mode = 'nearest',
    channel_shift_range = 10.
)

img = np.expand_dims(images[0], 0)
aug_iter = datagen.flow(img)
augmented_images = [next(aug_iter)[0].astype(np.uint8) for i in range(10)]"""

data_augmentation = tf.keras.Sequential([
    preprocessing.RandomRotation(0.2),
    preprocessing.RandomZoom(0.2),
])

# Convert images to grayscale and normalizing to [0,1]
images = color.rgb2gray(images) / 255.0
images = np.expand_dims(images, 3)
print(images.shape)
# Splitting data into training(0.8) and test(0.2) data's
train_img, test_img, train_labels, test_labels = train_test_split(images, labels, test_size = 0.2)

#print(train_img.shape)

### Building the Sequential Model
# Setting up layers
model = Sequential([
    # Dense: output = activation(dot(input, kernel "W matrix") + bias)
    data_augmentation,
    layers.Flatten(input_shape = (32, 32), name = 'Input'),  # Tranforms format of images from 2D->1D array
    layers.Dense(1024, activation = 'relu', name = 'Layer1'),# 1024 nodes
    layers.Dense(512, activation = 'relu', name = 'Layer2'), # 512 nodes
    layers.Dense(256, activation = 'relu', name = 'Layer3'), # 256 nodes
    layers.Dense(128, activation = 'relu', name = 'Layer4'), # 128 nodes
    layers.Dense(num_classes, name = "Output")]) # last layer (classes options)
# Compiling Model
model.compile(
    optimizer = 'adam', # how model is updated based on data and loss function
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True), # measures model accuracy
    metrics = ['accuracy']) # monitor training and testing steps

# Training model
epochs = 100
#history = model.fit(train_img, train_labels, batch_size = 200, epochs = epochs) #
history = model.fit(train_img, train_labels,
                    validation_data=(test_img, test_labels),
                    batch_size = batch_size,
                    epochs = epochs)

# Evaluate accuracy and score
test_loss, test_acc = model.evaluate(test_img, test_labels, verbose = 2)
print(f'\nTest Accuracy: {test_acc}')

# Making predictions
probability_model = Sequential([model, layers.Softmax()])
predictions = probability_model.predict(test_img) # array of numbers representing its confidence for each class

# Verifying predictions using test images and prediction arrays
score = []
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions[i], test_labels, test_img)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()

# Model Summary
model.summary() # DEBUG

# DEBUGGING MODELS
plot_graph()
plt.show()

"""
# Using trained model to test an image
img = tf.image.resize(img_to_array(load_img('stop.jpg')), (32,32))
img = np.expand_dims(img, 0)
print(img.shape)
predictions_single = probability_model.predict(img)
plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(9), class_names, rotation = 45)
plt.show()


img = tf.image.resize(mpimg.imread('stop.jpg'), (32, 32) # Import and resize
img = (np.expand_dims(color.rgb2gray(img), 0))  # Grayscale and turn to batch
img = np.expand_dims(img, 0)
predictions_single = probability_model.predict(img)
plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(9), class_names, rotation = 45)
print(np.argmax(predictions_single[0]))
plt.show()"""