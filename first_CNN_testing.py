""" from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from IPython.display import display
from PIL import Image  """
import numpy as np
from keras_preprocessing import image
from tensorflow import keras
from first_CNN_to_test import declaredatadets

classifier = keras.models.load_model('D:/NEA project/Networks/R.O.S.A - 2')

# train_datagen, training_set, test_set = declaredatadets()
'''
test_image = image.load_img("D:/NEA project/images/testing images/ALB1.jpg", target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] >= 0.5:
    prediction = "\n I believe that is an albatross"
else:
    prediction = "\n cannot tell what this is"
print(prediction)
'''
basePath = "D:/NEA project/images/testing images/"
baseName = "BD"

for i in range(37):
    path = basePath + baseName + str(i + 1) + ".jpg"
    test_image = image.load_img(path, target_size=(32, 32))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image) * 0.005
    # training_set.class_indices
    if result[0][0] >= 0.5:
        prediction = ": It is a bird"
    else:
        prediction = "Not a bird"
    print("BD", i, result[0][0], prediction)



