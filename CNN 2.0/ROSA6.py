from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from IPython.display import display
from PIL import Image
import numpy as np
from keras_preprocessing import image
from tensorflow import keras
import tensorflow as tf

ROSA6 = ""

train_datagen = ""
train_generator = ""
validation_generator = ""

img_size = (64, 64)
btch_size = 32

training_set = ""
validation_set = ""
train_datagen = ""


def make_network():
    global ROSA6

    ROSA6 = Sequential()
    # convolution layer:
    ROSA6.add(Convolution2D(64, 3, 3, input_shape=(64, 64, 3), activation='relu'))

    # pooling layer:
    ROSA6.add(MaxPooling2D(pool_size=(3, 3)))

    # flattening
    ROSA6.add(Flatten())

    # full connection
    # ROSA6.add(Dense(128, activation='relu'))
    # ROSA6.add(Dense(1, activation='sigmoid'))

    ROSA6.add(Dropout(0.5))

    #  compiling the CNN
    ROSA6.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    print("\n created network")
    save_network()


def load_network():
    global ROSA6
    ROSA6 = keras.models.load_model("D:/NEA project/Networks/R.O.S.A - 6")


def save_network():
    print("\n saving... ")
    ROSA6.save("D:/NEA project/Networks/R.O.S.A - 6")
    print("\n model saved \n")


def get_images():
    global training_set
    global validation_set
    global train_datagen

    '''
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

    training_set = train_datagen.flow_from_directory(
        'D:/NEA project/images/CUB_200_2011/rosa6_test/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary'
    )

    validation_set = test_datagen.flow_from_directory(
        'D:/NEA project/images/CUB_200_2011/rosa6_test/validation_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary'
    )
    '''
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.2)  # set validation split

    training_set = train_datagen.flow_from_directory(
        "D:/NEA project/images/CUB_200_2011/rosa6_test",
        target_size=img_size,
        batch_size=btch_size,
        class_mode='binary',
        subset='training')

    validation_set = train_datagen.flow_from_directory(
        "D:/NEA project/images/CUB_200_2011/rosa6_test",
        target_size=img_size,
        batch_size=btch_size,
        class_mode='binary',
        subset='validation')  # set as validation data


def train():
    ROSA6.fit_generator(
        training_set,
        steps_per_epoch=200,
        epochs=40,
        validation_data=validation_set,
        validation_steps=800)
    save_network()


def test_network():
    basePath = "D:/NEA project/images/testing images/"
    baseName = "BD"

    for i in range(37):
        path = basePath + baseName + str(i + 1) + ".jpg"
        test_image = image.load_img(path, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        answer = predict(test_image)
        print("BD", i + 1, predict(test_image))


def predict(image):
    result = ROSA6.predict(image)
    # training_set.class_indices
    temp_val = 1
    x = False
    for i in range(len(result[0]) - 1):
        if 0 < result[0][i] < 1:
            if result[0][i] < temp_val:
                temp_val = result[0][i]
    if temp_val > 0.01:
        x = True
    return temp_val, x  # , result[0][len(result)-1], result[0][1]


"""
    basePath = "D:/NEA project/images/testing images/"
    baseName = "BD"

    for i in range(37):
        path = basePath + baseName + str(i + 1) + ".jpg"
        test_image = image.load_img(path, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        probability_model = tf.keras.Sequential([ROSA6, tf.keras.layers.Softmax()])
        predictions = probability_model.predict(test_image)
        # validation_generator.class_indices
        '''if predictions[0] >= 0.5:
            prediction = ": It is a bird"
        else:
            prediction = "Not a bird"
        print("BD", i, result[0][0], prediction)'''
        print(predictions)
"""

'''
print("BD1")
test_image = image.load_img("D:/NEA project/images/testing images/BD1.jpg", target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = ROSA6.predict(test_image)
training_set.class_indices
print(len(result))
for i in result:
    print(i)
print(result[0])
'''

load_network()
