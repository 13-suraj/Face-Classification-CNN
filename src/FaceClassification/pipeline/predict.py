import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.keras"))

        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0) / 255.0  # normalize like training

        result = np.argmax(model.predict(test_image), axis=1)
        print("Raw prediction:", result)

        if result[0] == 1:
            prediction = "Subhash"
        else:
            prediction = "Suraj"

        return [{"image": prediction}]