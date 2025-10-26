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

        probs = model.predict(test_image)[0]

        class_idx = np.argmax(probs)
        confidence = float(probs[class_idx])

        labels = ["Subhash", "Suraj"]
        predicted_class = labels[class_idx]

        return {
            "class" : predicted_class,
            "confidence" : confidence,
            "probs" : {labels[i]: float(probs[i]) for i in range(len(labels))}
        }