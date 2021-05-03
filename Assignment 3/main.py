from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential, layers, optimizers
from pathlib import Path
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

def plot_graph(history, epochs):
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

def CNN_model():
    data_aug = ImageDataGenerator(
        rotation_range=30,
        zoom_range=0.3,
        width_shift_range=0.3,
        height_shift_range=0.3,
        shear_range=0.3,
        horizontal_flip=True,
        fill_mode="nearest")

    # Sequential Model
    model = Sequential()
    # Convolutional Layer 1
    model.add(layers.Conv2D(32, 3, activation='relu', input_shape=(32,32,3)))
    model.add(layers.Conv2D(32, 3, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Dropout(0.25))
    # Convolutional Layer 2
    model.add(layers.Conv2D(64, 3, activation='relu'))
    model.add(layers.Conv2D(64, 3, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Dropout(0.25))
    # Flattening
    model.add(layers.Flatten())
    # Fully connected layer
    model.add(layers.Dense(800, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(400, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(num_classes, activation='softmax'))

    opt = optimizers.Adam(learning_rate=0.001)

    # Compiling Model
    model.compile(
        optimizer=opt,  # how model is updated based on data and loss function
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),  # measures model accuracy
        metrics=['accuracy'])  # monitor training and testing steps

    # Training model
    epochs = 50
    CNN_history = model.fit(data_aug.flow(train_img, train_labels,
                                         batch_size=batch_size,
                                         shuffle=False),
                            epochs=epochs,
                            validation_data=(val_img, val_labels))
    # Model Summary
    model.summary()

    # Evaluate accuracy
    test_loss, test_acc = model.evaluate(test_img, test_labels, verbose=2)
    print(f'\nTest Accuracy: {test_acc}')

    # Training Plot
    plot_graph(CNN_history, epochs)

    ### Making predictions ###
    predictions = model.predict(test_img)  # array of numbers representing its confidence for each class

    # Verifying predictions using test images and prediction arrays
    num_rows = 5
    num_cols = 3
    num_images = num_rows * num_cols
    plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
    for i in range(num_images):
        plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
        plot_image(i, predictions[i], test_labels, test_img)
        plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
        plot_value_array(i, predictions[i], test_labels)
    plt.tight_layout()

    # show all plots
    plt.show()

    # Saving Model
    model.save('saved_model/CNN_model')

def API_model():
    data_aug = ImageDataGenerator(
        rotation_range=30,
        zoom_range=0.3,
        width_shift_range=0.3,
        height_shift_range=0.3,
        shear_range=0.3,
        horizontal_flip=True,
        fill_mode="nearest")

    inputs = tf.keras.Input(shape=(32, 32, 3))
    x = layers.Conv2D(32, 3)(inputs)
    x = layers.BatchNormalization()(x)
    x = tf.keras.activations.relu(x)
    x = layers.Conv2D(32, 3)(x)
    x = layers.BatchNormalization()(x)
    x = tf.keras.activations.relu(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Dropout(0.25)(x)

    x = layers.Conv2D(64, 3)(x)
    x = layers.BatchNormalization()(x)
    x = tf.keras.activations.relu(x)
    x = layers.Conv2D(64, 3)(x)
    x = layers.BatchNormalization()(x)
    x = tf.keras.activations.relu(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Dropout(0.25)(x)

    x = layers.Flatten()(x)

    x = layers.Dense(800, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(400, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(200, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)

    model = tf.keras.Model(inputs=inputs, outputs=outputs)

    opt = optimizers.Adam(learning_rate=0.001)

    # Compiling Model
    model.compile(
        optimizer=opt,  # how model is updated based on data and loss function
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),  # measures model accuracy
        metrics=['accuracy'])  # monitor training and testing steps

    # Training model
    epochs = 50
    # history = model.fit(train_img, train_labels, batch_size = 200, epochs = epochs) #
    CNN_history = model.fit(data_aug.flow(train_img, train_labels,
                                          batch_size=batch_size,
                                          shuffle=False),
                            epochs=epochs,
                            validation_data=(val_img, val_labels))

    # Model Summary
    model.summary()

    # Evaluate accuracy
    test_loss, test_acc = model.evaluate(test_img, test_labels, verbose=2)
    print(f'\nTest Accuracy: {test_acc}')

    # Training Plot
    plot_graph(CNN_history, epochs)

    ### Making predictions ###
    predictions = model.predict(test_img)  # array of numbers representing its confidence for each class

    # Verifying predictions using test images and prediction arrays
    num_rows = 5
    num_cols = 3
    num_images = num_rows * num_cols
    plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
    for i in range(num_images):
        plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
        plot_image(i, predictions[i], test_labels, test_img)
        plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
        plot_value_array(i, predictions[i], test_labels)
    plt.tight_layout()

    # show all plots
    plt.show()

if __name__ == '__main__':
    # Initial Parameters
    num_classes = 9
    num_images = 11429
    img_height = 32
    img_width = 32
    batch_size = 128

    train_ratio = 0.75
    validation_ratio = 0.15
    test_ratio = 0.1

    class_names = ['30km/hr', '50km/hr', '70km/hr', '80km/hr', '100km/hr', 'Stop', 'Turn Right',
                   'Turn Left', 'Straight']

    data_dir = Path('Traffic Data')

    # Importing images and labels into dataset
    dataset = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        seed=123,
        image_size=(img_height, img_width),
        batch_size=num_images)

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
        images, labels, test_size= 1 - train_ratio)
    val_img, test_img, val_labels, test_labels = train_test_split(
        test_img, test_labels, test_size=test_ratio / (test_ratio + validation_ratio))

    # Uncomment which model to train and test
    CNN_model()
    #API_model()