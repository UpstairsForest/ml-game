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

epochs = 10
for e in range(epochs):
    model.fit(train_images, train_labels, epochs=1, verbose=1)
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

# Predictions
prob_model = tf.keras.Sequential([
    model,  # keeps the weights
    tf.keras.layers.Softmax(),  # turn whatever previous layer outputs into nice probabilities
])
predictions = prob_model.predict(test_images)


def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                         100 * np.max(predictions_array),
                                         class_names[true_label]),
               color=color)


def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    this_plot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    this_plot[predicted_label].set_color('red')
    this_plot[true_label].set_color('blue')


i = np.random.choice([i for i in range(len(test_images))])
plt.figure(figsize=(6, 3))
plt.subplot(1, 2, 1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1, 2, 2)
plot_value_array(i, predictions[i], test_labels)
plt.show()
