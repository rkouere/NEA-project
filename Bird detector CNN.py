from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from IPython.display import display
from PIL import Image
import numpy as np
from keras_preprocessing import image
from tensorflow import keras

ROSA2 = ""


def makenetwork():
    ROSA2 = Sequential()

    # convolution:
    ROSA2.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation='relu'))

    # pooling:
    ROSA2.add(MaxPooling2D(pool_size=(2, 2)))

    # flattening
    ROSA2.add(Flatten())

    # full connection
    ROSA2.add(Dense(128, activation='relu'))
    ROSA2.add(Dense(1, activation='sigmoid'))

    #  compiling the CNN
    ROSA2.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    ROSA2.save("D:/NEA project/Networks/R.O.S.A - 2")


def loadnetwork():
    global ROSA2
    ROSA2 = keras.models.load_model('D:/NEA project/Networks/R.O.S.A - 2')


def declaredatadets():
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

    training_set = train_datagen.flow_from_directory(
        'D:/NEA project/images/CUB_200_2011/images',
        target_size=(64, 64),
        batch_size=575,
        class_mode='binary'
    )

    test_set = test_datagen.flow_from_directory(
        'D:/NEA project/images/CUB_200_2011/testing images',
        target_size=(64, 64),
        batch_size=119,
        class_mode='binary'
    )
    return train_datagen, training_set, test_set


def train(training_set, test_set):
    ROSA2.fit(
        training_set,
        steps_per_epoch=20,
        epochs=20,
        validation_data=test_set,
        validation_steps=12)

    ROSA2.save("D:/NEA project/Networks/R.O.S.A - 2")



def recimage(imgpath):
    train_datagen, training_set, test_set = declaredatadets()
    test_image = image.load_img(imgpath, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = ROSA2.predict(test_image)
    training_set.class_indices
    if result[0][0] >= 0.5:
        prediction = "\n, This is a bird"
    else:
        prediction = "\n, I do not think it is a bird"
    print(result, prediction)


loadnetwork()
"""
train_datagen, training_set, test_set = declaredatadets()
train(training_set, test_set)
"""
recimage("D:/NEA project/images/testing images/ALB1.jpg")
