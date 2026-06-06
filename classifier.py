import numpy as np
import tensorflow as tf


IMAGE_SIZE = (150, 150)

CLASS_NAMES = ["buildings", "forest", "sea"]


def load_and_preprocess_image(path: str):
    image = tf.keras.preprocessing.image.load_img(path, target_size=IMAGE_SIZE)

    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)

    return img_array


def classify(model, image_path: str):
    preprocessed_image = load_and_preprocess_image(image_path)

    predictions = model.predict(preprocessed_image, verbose=0)

    predicted_index = int(np.argmax(predictions[0]))
    label = CLASS_NAMES[predicted_index]
    probability = float(predictions[0][predicted_index])

    return label, probability
