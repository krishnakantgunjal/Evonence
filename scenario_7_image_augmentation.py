# Scenario 7: Image Augmentation
# Task: Use TensorFlow/Keras to 
# create an image augmentation pipeline 
# with random rotations (±20 degrees), horizontal flips, and zoom (0.2x).

import tensorflow as tf
from tensorflow.keras import layers

data_augmentation = tf.keras.Sequential([
    layers.RandomRotation(0.2),
    layers.RandomFlip("horizontal"),
    layers.RandomZoom(0.2)
])
