from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

img_2 = np.array(Image.open(r"D:\NEA project\images\Simba.png"))

n, bins, patches = plt.hist(img_2.flatten(), bins=range(256))
plt.show()

corrected_image = ImageOps.autocontrast(img_2)