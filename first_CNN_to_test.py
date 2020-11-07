from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from IPython.display import display
from PIL import Image
import numpy as np
from keras_preprocessing import image
from tensorflow import keras

classifier = keras.models.load_model('D:/NEA project/Networks/R.O.S.A - 1')


def makenetwork():
    # convolution layer:
    classifier.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation='relu'))

    # pooling layer:
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    # flattening
    classifier.add(Flatten())

    # full connection
    classifier.add(Dense(128, activation='relu'))
    classifier.add(Dense(1, activation='sigmoid'))

    #  compiling the CNN
    classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# fitting CNN to the images
def declaredatadets():
    global train_datagen
    global training_set

    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

    training_set = train_datagen.flow_from_directory(
        'D:/NEA project/images/CUB_200_2011/testing images/training',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary'
    )

    test_set = test_datagen.flow_from_directory(
        'D:/NEA project/images/CUB_200_2011/testing images',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary'
    )
    return train_datagen, training_set, test_set


def train():
    classifier.fit_generator(
        training_set,
        steps_per_epoch=8000,
        epochs=10,
        validation_data=test_set,
        validation_steps=800)


def main(imgpath):
    declaredatadets()
    test_image = image.load_img(imgpath, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    training_set.class_indices
    if result[0][0] >= 0.5:
        prediction = "Albatross is right"
    else:
        prediction = "yeah no clue mate"
    print(prediction)

    classifier.save("D:/NEA project/Networks")

