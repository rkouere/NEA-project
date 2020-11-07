from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r"D:\NEA project\images\Simba.png")  # imports the image
w, h = img.size   # gets the width and height of the image

print("width : {} px, height : {} px".format(w, h))  # imply outputs image dimensions

print("Pixel format: {}".format(img.mode))  # "L" means intensity is coded in 8 bits

px_values = img.getpixel((20, 100))
print("Values in pixels in (20,100) : {}".format(px_values))

mat = np.array(img)  # note that x and y values are flipped in an array ( it is [y][x] not [x][y])
print(mat)

print("size of matrix in pixels : {}".format(mat.shape))
