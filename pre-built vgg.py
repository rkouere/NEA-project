from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions

model = VGG16()  # Création du modèle VGG-16 implementé par Keras
"""
img = load_img('D:/NEA project/images/testing images/BD15.jpg', target_size=(224, 224))  # Charger l'image
img = img_to_array(img)  # Convertir en tableau numpy
img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))  # Créer la collection d'images (un seul échantillon)
img = preprocess_input(img)  # Prétraiter l'image comme le veut VGG-16

y = model.predict(img)  # Prédir la classe de l'image (parmi les 1000 classes d'ImageNet)

# Afficher les 3 classes les plus probables
print('Top 3 :', decode_predictions(y, top=3)[0])
"""


def test_network():
    basePath = "D:/NEA project/images/testing images/"
    baseName = "BD"
    img = load_img("D:/NEA-project/mimi.JPG", target_size=(224, 224))  # Charger l'image
    img = img_to_array(img)  # Convertir en tableau numpy
    img = img.reshape(
        (1, img.shape[0], img.shape[1], img.shape[2]))  # Créer la collection d'images (un seul échantillon)
    img = preprocess_input(img)  # Prétraiter l'image comme le veut VGG-16
    # for i in range(37):
    #     path = basePath + baseName + str(i + 1) + ".jpg"
    #     img = load_img(path, target_size=(224, 224))  # Charger l'image
    #     img = img_to_array(img)  # Convertir en tableau numpy
    #     img = img.reshape(
    #         (1, img.shape[0], img.shape[1], img.shape[2]))  # Créer la collection d'images (un seul échantillon)
    #     img = preprocess_input(img)  # Prétraiter l'image comme le veut VGG-16
    #
    #     y = model.predict(img)  # Prédir la classe de l'image (parmi les 1000 classes d'ImageNet)
    #
    #     # Afficher les 3 classes les plus probables
    #     print('Top 1000 :', decode_predictions(y, top=1000)[0])

    y = model.predict(img)  # Prédir la classe de l'image (parmi les 1000 classes d'ImageNet)

    # Afficher les 3 classes les plus probables
    decoded_array = []
    x = decode_predictions(y, top=3)
    for i in x[0]:
        print(i[1])
        decoded_array.append(i[1])

    return decoded_array


print(test_network())
