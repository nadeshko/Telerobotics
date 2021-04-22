from tensorflow.keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from tensorflow.keras.layers.experimental import preprocessing
from tensorflow.keras import Sequential, layers
from pathlib import Path
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

def get_ds():
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=1 - train_ratio,
        subset="training",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=validation_ratio,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    test_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=test_ratio,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    return train_ds, val_ds, test_ds

def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    predicted_label = np.argmax(predictions_array)

    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow((img*255).astype(np.uint8))

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
test_ratio = 0.10

data_dir = Path('Traffic Data')

# Import images and labels to datasets
train_ds, val_ds, test_ds = get_ds()
labels = train_ds.class_names
class_names = ['30km/hr','50km/hr','70km/hr', '80km/hr','100km/hr', 'Stop', 'Turn Right',
               'Turn Left', 'Straight']

# Resize and Rescale model
resize_N_rescale = Sequential([
    preprocessing.Rescaling(img_height,img_width),
    preprocessing.Rescaling(1./255)])

# Creating the model
model = Sequential([
    resize_N_rescale,
    layers.Conv2D(32, (2, 2), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, (2, 2), activation='relu', padding='same'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, (2, 2), activation='relu', padding='same'),
    layers.Dense(128, activation = 'relu', name = 'Layer2'), # 128 nodes
    layers.Dense(num_classes, activation='softmax')
])

model.compile(
    optimizer = 'adam', # how model is updated based on data and loss function
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True), # measures model accuracy
    metrics = ['accuracy']) # monitor training and testing steps

epochs = 10
history = model.fit(train_ds,
                    validation_data=val_ds,
                    batch_size = batch_size,
                    epochs = epochs)

test_loss, test_acc = model.evaluate(test_ds)
print(f'\nTest Accuracy: {test_acc}')

model.summary()

# Making predictions
probability_model = Sequential([model, layers.Softmax()])
predictions = probability_model.predict(test_ds) # array of numbers representing its confidence for each class

"""
# Verifying predictions using test images and prediction arrays
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for images, labels in test_ds.take(1):
    for i in range(num_images):
        plt.subplot(num_rows, 2*num_cols, 2*i+1)
        plot_image(i, predictions[i], labels, images)
        plt.subplot(num_rows, 2*num_cols, 2*i+2)
        plot_value_array(i, predictions[i], labels)
    plt.tight_layout()

# Model Summary
model.summary()

plt.show()"""