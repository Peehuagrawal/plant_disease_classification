import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os
import json

# Load model
MODEL_PATH = os.path.join("model", "plant_disease_model.h5")
model = load_model(MODEL_PATH)

# Load class indices (reverse mapping from index to class name)
CLASS_INDEX_PATH = os.path.join("model", "class_indices.json")
with open(CLASS_INDEX_PATH, "r") as f:
    class_indices = json.load(f)

# Invert the class_indices dictionary to get index → class name
class_names = [None] * len(class_indices)
for class_name, index in class_indices.items():
    class_names[index] = class_name

# Prediction function
def predict_disease(image_path):
    img = load_img(image_path, target_size=(128, 128))
    img_array = img_to_array(img) / 255.0  # Must match training
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    pred_index = np.argmax(preds[0])
    predicted_class = class_names[pred_index]
    confidence = float(np.max(preds))

    return predicted_class, confidence
