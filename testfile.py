import keras
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from IPython.display import display
from PIL import Image
import numpy as np
from keras_preprocessing import image
from tensorflow import keras

ROSA5 = ""
train_datagen = ""
train_generator = ""
validation_generator = ""

img_size = (180, 180)
btch_size = 16


def makenetwork():
    global ROSA5
    ROSA5 = Sequential()

    # I'm not going to use a fully-connected layer

    # Adding of first convolution layer, followed by a layer of ReLu
    # .                    v filter w/ 3x3 dimensions
    ROSA5.add(Conv2D(16, (3, 3), input_shape=(180, 180, 3), padding="same", activation="relu"))
    # .               ^64 filters (K)                                 ^ it conserves the size of the input volume
    ROSA5.add(MaxPooling2D())
    #  for padding: "valid" would decrease the input volume. We never use "Valid"
    # ReLu means that any input under 0 will output as 0, and any input over 0 will output the same value as their input
    # adding of second convolution layer, which is then followed by a layer of ReLu
    ROSA5.add(Conv2D(32, (3, 3), padding='same', activation='relu'))

    ROSA5.add(MaxPooling2D())

    ROSA5.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    # Addition of first pooling layer:
    ROSA5.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

    """ what pooling and its parameters do: 
    Downsamples the input representation by taking the maximum value over the window defined by pool_size 
    for each dimension along the features axis. The window is shifted by strides in each dimension.
    from https://keras.io/api/layers/pooling_layers/max_pooling2d/"""

    ROSA5.add(Flatten())

    ROSA5.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    ROSA5.save("D:/NEA project/Networks/R.O.S.A - 5")


train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.21)  # set validation split

train_generator = train_datagen.flow_from_directory(
    "D:/NEA project/images/CUB_200_2011/images",
    target_size=img_size,
    batch_size=btch_size,
    class_mode='binary',
    subset='training')

validation_generator = train_datagen.flow_from_directory(
    "D:/NEA project/images/CUB_200_2011/images",
    target_size=img_size,
    batch_size=btch_size,
    class_mode='binary',
    subset='validation')  # set as validation data

makenetwork()


def testnetwork():
    basePath = "D:/NEA project/images/testing images/"
    baseName = "BD"

    for i in range(37):
        path = basePath + baseName + str(i + 1) + ".jpg"
        test_image = image.load_img(path, target_size=(32, 32))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = ROSA5.predict(test_image) * 0.0005
        validation_generator.class_indices
        if result[0][0] >= 0.5:
            prediction = ": It is a bird"
        else:
            prediction = "Not a bird"
        print("BD", i, result[0][0], prediction)


testnetwork()


for i in range(12):
    print(i)