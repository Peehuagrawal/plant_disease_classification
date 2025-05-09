# 🌿 Plant Disease Detection Web App

A deep learning-powered Flask application that detects plant leaf diseases from uploaded images using a Convolutional Neural Network (CNN) trained on the [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease).

This project was built to apply computer vision for agriculture and to understand the end-to-end deployment of AI models in real-world web applications.

---

## 🚀 Features

- 🔍 Detects plant diseases from leaf images
- 🧠 Built on a custom-trained CNN using TensorFlow and Keras
- 🔄 Automatically loads correct class labels from `class_indices.json`
- 🧪 Trained with extensive data augmentation and regularization
- 🌐 Flask-based interface for real-time prediction
- 💾 Displays prediction confidence and shows uploaded image

---


## 🏗️ Project Structure

```
plant_disease_flask_app/
├── app.py                      # Flask backend
├── utils.py                    # Prediction logic
├── model/
│   ├── plant_disease_model.h5  # Trained Keras model
│   └── class_indices.json      # Class index to name mapping
├── static/
│   └── uploads/                # Uploaded leaf images
├── templates/
│   └── index.html              # Upload form and prediction display
├── requirements.txt            # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/plant-disease-flask-app.git
cd plant-disease-flask-app
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate     # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Model Files
Copy the following into the `model/` folder:
- `plant_disease_model.h5` (your trained model)
- `class_indices.json` (saved from training)

### 5. Run the App
```bash
python app.py
```

Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 Model Training Summary

The model was trained on a subset of the PlantVillage dataset using:
- Convolutional Neural Network (CNN)
- Batch Normalization and Dropout
- L2 Regularization to reduce overfitting
- `ImageDataGenerator` for advanced augmentation

📊 Achieved **>91% validation accuracy** using TensorFlow + Keras.

---

## 🛠️ Future Improvements

- Display top-3 predictions with confidence
- Show per-class probability scores
- Add user feedback loop for validation
- Mobile-optimized UI
- Host via Render / Railway / Hugging Face Spaces

---

## 🗒️ Notes

- This project was built as part of my deep learning exploration and hands-on deployment journey.
- The model is fully offline — all inference happens in the backend using TensorFlow.
- Designed to scale with new classes or retrained models — just update `.h5` and `class_indices.json`.

---

## 📚 Acknowledgements

- [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)
- TensorFlow & Keras open-source contributors
- Everyone who supports open and accessible AI for agriculture

---

## 🌱 Made with 💡 and Python by [Peehu Agrawal](https://github.com/yourusername)

Feel free to ⭐️ this repo, fork it, or open issues for suggestions and feedback!
