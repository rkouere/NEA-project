from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from IPython.display import display
from PIL import Image
import numpy as np
from keras_preprocessing import image
from tensorflow import keras
import tensorflow as tf

ROSA5 = ""

train_datagen = ""
train_generator = ""
validation_generator = ""

img_size = (128, 128)
btch_size = 64


def make_network():
    global ROSA5

    ROSA5 = Sequential()
    # convolution layer:
    ROSA5.add(Convolution2D(32, 3, 3, input_shape=(128, 128, 3), activation='relu'))

    # pooling layer:
    ROSA5.add(MaxPooling2D(pool_size=(2, 2)))

    # flattening
    ROSA5.add(Flatten())

    ROSA5.add(Dropout(0.8, noise_shape=None, seed=None))

    # full connection
    ROSA5.add(Dense(128, activation='relu'))
    ROSA5.add(Dense(1, activation='sigmoid'))

    #  compiling the CNN
    ROSA5.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    ROSA5.save("D:/NEA project/Networks/R.O.S.A - 5")


def load_network():
    global ROSA5
    ROSA5 = keras.models.load_model("D:/NEA project/Networks/R.O.S.A - 5")


def get_images():
    global train_datagen
    global train_generator
    global validation_generator
    global img_size
    global btch_size
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.25)  # set validation split

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


def train():
    ROSA5.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // btch_size,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // btch_size,
        epochs=50)
    ROSA5.save("D:/NEA project/Networks/R.O.S.A - 5")


def testnetwork():
    basePath = "D:/NEA project/images/testing images/"
    baseName = "BD"

    for i in range(37):
        path = basePath + baseName + str(i + 1) + ".jpg"
        test_image = image.load_img(path, target_size=(128, 128))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        probability_model = tf.keras.Sequential([ROSA5, tf.keras.layers.Softmax()])
        predictions = probability_model.predict(test_image)
        # validation_generator.class_indices
        '''if predictions[0] >= 0.5:
            prediction = ": It is a bird"
        else:
            prediction = "Not a bird"
        print("BD", i, result[0][0], prediction)'''
        print(predictions)


#make_network()
get_images()
print(train_generator.samples, validation_generator.samples, train_generator.samples // btch_size)
#train()
#testnetwork()
