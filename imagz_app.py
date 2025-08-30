import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load trained model

model = load_model("model.h5")

# Class labels
class_names = ['Cat', 'Dog']

# Page setup
st.set_page_config(page_title="Cat vs Dog Classifier", layout="centered")
st.title("🐱🐶 Cat vs Dog Classifier")
st.write("Upload an image and get the prediction!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).resize((32, 32))
    st.image(image, caption='Uploaded Image', use_container_width=True)

    # Preprocess image
    image_array = np.array(image) / 255.0
    prediction = model.predict(np.expand_dims(image_array, axis=0))

    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    st.success(f"Prediction: **{predicted_class}** ({confidence:.2f}% confidence)")
