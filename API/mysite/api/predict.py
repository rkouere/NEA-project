from django.conf import settings
from django.core.files.storage import default_storage
import os
from keras_preprocessing import image
import numpy as np
import keras
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
import json
import urllib.request
from keras.preprocessing.image import load_img, img_to_array
import base64

ROSA6 = ""
VGG_16 = ""
bird_array = []


# Loads both of the neural networks
def load_networks():
    '''
    banane
    Returns:

    '''
    global ROSA6, VGG_16
    # load my neural network through a directory
    ROSA6 = keras.models.load_model("../../Networks/R.O.S.A - 6")

    # load the pre built network, VGG-16:
    VGG_16 = VGG16()


# Predicts what the image is through my neural network and returns a boolean
def predict_ROSA(data):
    global ROSA6, VGG_16

    # the whole predicting still requires tweaking
    result = ROSA6.predict(data)
    temp_val = 1
    x = False
    for i in range(len(result[0]) - 1):
        if 0 < result[0][i] < 1:
            if result[0][i] < temp_val:
                temp_val = result[0][i]
    if temp_val > 0.01:
        return True
    else:
        return False


# Predicts what the image is through VGG-16 and returns a boolean
def predict_VGG(data):
    # predict the value using ".predict"
    raw_predictions = VGG_16.predict(data)

    # only using ".predict" will give unreadable data, the function "decode_predictions" is needed to decode the data
    decoded_prediction = decode_predictions(raw_predictions, top=1)[0][0][1]

    return decoded_prediction


# This object is what the image is, its main purpose is to convert a jpg image into a Keras image object
class UploadedImage:

    def __init__(self, data):
        """
        Args:
            data: contains the base 64 string which represents the uploaded image
        """
        self.path = "../../API/mysite/temp-images/temp.jpg"
        self.img = data

        # Separate images needed because ROSA6 and VGG-16 work with different target sizes
        self.ROSA_image = ""
        self.VGG_image = ""

    def save_image(self, data):
        """
        saves the image into a directory so that I can make it into a keras object

        Args:
            data: contains the converted image file
        """

        filename = self.path
        with open(filename, 'wb') as f:
            f.write(data)

    def keras(self):
        # loads the temporary image file I created into keras objects to be processed
        self.ROSA_image = image.load_img(self.path, target_size=(64, 64))
        self.VGG_image = image.load_img(self.path, target_size=(224, 224))
        self.convert_to_array()

    def delete(self):
        # deletes the temporary image file to avoid having overlapping files
        os.remove(self.path)

    def convert(self):
        # Converts the base 64 string into an image
        imageData = base64.b64decode(self.img)
        self.save_image(imageData)
        self.keras()
        self.delete()

    def convert_to_array(self):
        # keras processes images that are in array form, so I need to convert them to arrays
        self.ROSA_image = image.img_to_array(self.ROSA_image)
        self.ROSA_image = np.expand_dims(self.ROSA_image, axis=0)

        self.VGG_image = image.img_to_array(self.VGG_image)
        self.VGG_image = self.VGG_image.reshape(
            (1, self.VGG_image.shape[0], self.VGG_image.shape[1], self.VGG_image.shape[2]))
        self.VGG_image = preprocess_input(self.VGG_image)  # Pre-treats the image in the form that VGG_16 accepts

    def predict(self):
        return predict_ROSA(self.ROSA_image), predict_VGG(self.VGG_image)


load_networks()
