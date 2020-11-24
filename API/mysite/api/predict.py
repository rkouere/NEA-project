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

ROSA6 = ""
VGG_16 = ""


def load_networks():
    global ROSA6, VGG_16
    # load my neural network
    ROSA6 = keras.models.load_model("../../Networks/R.O.S.A - 6")

    # load the pre built network, VGG-16:
    VGG_16 = VGG16()


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
        x = True
    return temp_val, x


def predict_VGG(data):
    # predict the value using ".predict"
    raw_predictions = VGG_16.predict(data)

    # only using ".predict" will give unreadable data, the function "decode_predictions" is needed to decode the data
    decoded_prediction = decode_predictions(raw_predictions, top=1)[0][0][1]
    return decoded_prediction


def get_database_data():
    bird_array = []

    with urllib.request.urlopen("http://127.0.0.1:8000/bird") as url:
        data = json.loads(url.read().decode())

    for i in data:
        list1 = i.values()
        list_list = list(list1)
        bird_array.append(list_list[1])
    return bird_array


class UploadedImage:

    def __init__(self, data, data_type):
        # make different methods for jpg and png, if errors would occur
        if data_type == "jpg":
            self.path = "../../API/mysite/temp-images/tmp.jpg"
            print("jpg")
        elif data_type == "png":
            self.path = "../../API/mysite/temp-images/tmp.png"
            print("png")
        self.img = data
        self.datatype = data_type

        # Separate images needed because ROSA6 and VGG-16 work with different target sizes
        self.ROSA_image = ""
        self.VGG_image = ""

    def save_image(self):
        # save the image into a directory so that I can make it into a keras object
        path = default_storage.save(self.path, self.img)
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

    def keras(self):
        # loads the temporary image file I created
        self.ROSA_image = image.load_img(self.path, target_size=(64, 64))
        self.VGG_image = image.load_img(self.path, target_size=(224, 224))
        self.convert_to_array()

    def delete(self):
        # deletes the temporary image file to avoid having overlapping files
        os.remove(self.path)

    def convert(self):
        self.save_image()
        self.keras()
        self.delete()
        # print(self.ROSA_image, self.VGG_image)

    def convert_to_array(self):
        # keras processes images that are in array form, so I need to convert them to arrays
        self.ROSA_image = image.img_to_array(self.ROSA_image)
        self.ROSA_image = np.expand_dims(self.ROSA_image, axis=0)

        self.VGG_image = image.img_to_array(self.VGG_image)
        self.VGG_image = self.VGG_image.reshape(
            (1, self.VGG_image.shape[0], self.VGG_image.shape[1], self.VGG_image.shape[2]))
        self.VGG_image = preprocess_input(self.VGG_image)  # Pre-treats the image like VGG_16 likes

    def predict(self):
        return predict_ROSA(self.ROSA_image), predict_VGG(self.VGG_image)


load_networks()
