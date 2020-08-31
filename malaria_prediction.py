import tensorflow as tf
from tensorflow import keras
import numpy as np
import PIL.Image

model = keras.models.load_model("models/malaria_model_94")

class_names = ["Parasitized", "Uninfected"]


def predict_image(path, img_height=150, img_width=150):
    img = keras.preprocessing.image.load_img(path, target_size=(img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    #   print(
    #       "This image most likely belongs to {} with a {} percent confidence."
    #       .format(class_names[np.argmax(score)], 100 * np.max(score))
    #   )
    return [(class_names[np.argmax(score)]), 100 * np.max(score)]


def resize_image(path, new_width=150, new_height=150):
    im = PIL.Image.open(path)
    if im.size != (new_width, new_height):
        im = im.resize((new_width, new_height))
        im.save(path)


def predict(path):
    resize_image(path)
    return predict_image(path)


if __name__ == "__main__":
    resize_image("parasite.png")
    print(predict_image("parasite.png"))
