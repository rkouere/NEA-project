from django.conf import settings
from django.core.files.storage import default_storage
import os
from keras_preprocessing import image
import numpy as np
import keras
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.preprocessing.image import load_img, img_to_array

ROSA6 = ""
VGG_16 = ""


def load_networks():
    global ROSA6, VGG_16
    ROSA6 = keras.models.load_model("D:/NEA-project/Networks/R.O.S.A - 6")

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
    y = VGG_16.predict(data)  # predicts what it thinks it is

    # returns the most probable outcome
    return decode_predictions(y, top=1)[0]


class UploadedImage:

    def __init__(self, data, data_type):
        if data_type == "jpg":
            self.path = "D:/NEA-project/API/mysite/temp-images/tmp.jpg"
            print("jpg")
        elif data_type == "png":
            self.path = "D:/NEA-project/API/mysite/temp-images/tmp.png"
            print("png")
        self.img = data
        self.datatype = data_type

        # Separate images needed because ROSA6 and VGG-16 work with different target sizes
        self.ROSA_image = ""
        self.VGG_image = ""

    def save_image(self):
        path = default_storage.save(self.path, self.img)
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

    def keras(self):
        self.ROSA_image = image.load_img(self.path, target_size=(64, 64))
        self.VGG_image = image.load_img(self.path, target_size=(224, 224))
        self.convert_to_array()

    def delete(self):
        os.remove(self.path)

    def convert(self):
        self.save_image()
        self.keras()
        self.delete()
        # print(self.ROSA_image, self.VGG_image)

    def convert_to_array(self):
        self.ROSA_image = image.img_to_array(self.ROSA_image)
        self.ROSA_image = np.expand_dims(self.ROSA_image, axis=0)

        self.VGG_image = image.img_to_array(self.VGG_image)
        self.VGG_image = self.VGG_image.reshape(
            (1, self.VGG_image.shape[0], self.VGG_image.shape[1], self.VGG_image.shape[2]))
        self.VGG_image = preprocess_input(self.VGG_image)  # Pre-treats the image like VGG_16 likes

    def predict(self):
        return predict_ROSA(self.ROSA_image), predict_VGG(self.VGG_image)


starter = open("D:/NEA-project/API/mysite/predict startup.txt", "r+")
contents = starter.read()
if contents == "0":
    ROSA6 = ""
    VGG_16 = ""
    starter.truncate()
    load_networks()
elif contents == "1":
    pass
