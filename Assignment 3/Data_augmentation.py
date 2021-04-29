from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import matplotlib.pyplot as plt
import numpy as np

aug = ImageDataGenerator(
        rotation_range=30,
        zoom_range=0.15,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.15,
        horizontal_flip=True,
        fill_mode="nearest")

train_generator = aug.flow_from_directory(
                  directory='Traffic Data/',
                  target_size=(32, 32), # resize to this size
                  color_mode="rgb", # for coloured images
                  batch_size=5, # number of images to extract from folder for every batch
                  class_mode="binary", # classes to predict
                  seed=2020 # to make the result reproducible
                  )

plt.figure(figsize=(10, 10))
for i in range(9):
    # convert to unsigned integers for plotting
    image = next(train_generator)[0].astype('uint8')
    augmented_image = aug(image)
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(augmented_image[0])
    plt.axis("off")

plt.show()