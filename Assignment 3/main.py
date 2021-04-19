import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import glob
from pathlib import Path

labels_csv = pd.read_csv('labels.csv')
data_dir = Path('Datasets/')

images, labels = [], []
for filename in glob.glob('Datasets/0/*.png'):
    im = Image.open(filename)
    data = np.asarray(im)
    images.append(data)

print(images[0].shape)

image_count = len(list(data_dir.glob('*/*.png')))
print(image_count)


