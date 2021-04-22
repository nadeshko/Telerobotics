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
batch_size = 50

train_ratio = 0.75
validation_ratio = 0.15
test_ratio = 0.10

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

# Convert images to grayscale and normalizing to [0,1]
images = images / 255.0

# Splitting data into training(0.75), validation(0.15), and test(0.1) data sets
train_img, test_img, train_labels, test_labels = train_test_split(
    images, labels, test_size = 1 - train_ratio)
val_img, test_img, val_labels, test_labels = train_test_split(
    test_img, test_labels, test_size = test_ratio / (test_ratio + validation_ratio))

data_augmentation = Sequential([
    layers.experimental.preprocessing.RandomRotation(0.3, input_shape=(32, 32, 3)),
    layers.experimental.preprocessing.RandomZoom(0.3)])

model = Sequential([
    data_augmentation,
    layers.Conv2D(32, 3, activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2), strides=2, name='MaxPooling1'),
    layers.Conv2D(64, 3, activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2), strides=2, name='MaxPooling2'),
    layers.Conv2D(64, 3, activation='relu', padding='same'),
    layers.Dropout(0.2),
    layers.Flatten(),
    layers.Dense(128, activation = 'relu', name = 'Layer'), # 128 nodes#
    layers.Dense(num_classes, activation='softmax',name="Output")]) # last layer (classes options)

# Compiling Model
model.compile(
    optimizer = 'adam', # how model is updated based on data and loss function
    loss = tf.keras.losses.SparseCategoricalCrossentropy(), # measures model accuracy
    metrics = ['accuracy']) # monitor training and testing steps

# Training model
epochs = 10
#history = model.fit(train_img, train_labels, batch_size = 200, epochs = epochs) #
history = model.fit(train_img, train_labels,
                    validation_data=(val_img, val_labels),
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=2)

# Evaluate accuracy and score
test_loss, test_acc = model.evaluate(test_img, test_labels, verbose=2)
print(f'\nTest Accuracy: {test_acc}')

# Making predictions
#probability_model = Sequential([model, layers.Softmax()])
predictions = model.predict(test_img) # array of numbers representing its confidence for each class

# Verifying predictions using test images and prediction arrays
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


#img = load_img('stop.jpg', target_size=(img_height, img_width))
#img = np.expand_dims(img_to_array(img), 0)
#print(img.shape)
img = np.expand_dims(test_img[22], 0)
plt.figure()
plt.imshow(test_img[22])
predictions_single = model.predict(img)
score = tf.nn.softmax(predictions_single[0])
plt.figure()
plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(9), class_names, rotation = 45)

plt.show()
"""
# Using trained model to test an image
img = tf.image.resize(img_to_array(load_img('stop.jpg')), (32,32))
img = np.expand_dims(img, 0)
print(img.shape)
predictions_single = model.predict(img)
plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(9), class_names, rotation = 45)
plt.show()"""