from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from IPython.display import display
from PIL import Image
import numpy as np
from keras_preprocessing import image
from tensorflow import keras

classifier = keras.models.load_model('D:/NEA project/Networks')

