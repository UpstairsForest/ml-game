# https://www.tensorflow.org/tutorials/keras/classification

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Data
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images, test_images = train_images / 255.0, test_images / 255.0

# Model setup
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # flatten inputs from 28, 28 to 784
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10),  # every input is connected to every output by weights
])
model.compile(
    # measures how accurate the model is during training, loss is minimized
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    # determines the model is updated based on data it sees and its loss function
    optimizer="adam",
    # for monitoring the training
    metrics=["accuracy"]
)

# Train
model.fit(train_images, train_labels, epochs=20, verbose=1)

# Evaluate
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
