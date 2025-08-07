import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load your trained CNN model
model = load_model('model/cnn_model.h5')  # Update path as needed

# Define class names (change based on your dataset)
class_names = ['Cat', 'Dog']  # Replace with your actual class labels

# Set page config
st.set_page_config(page_title="Image Classification CNN", layout="centered")

# Title
st.title("🧠 Image Classification using CNN")
st.markdown("Upload an image and the model will predict its class.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Preprocess image
    st.write("Classifying...")
    img = img.resize((64, 64))  # Ensure this matches model input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize if model was trained on normalized data

    # Predict
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    # Output
    st.success(f"Prediction: **{predicted_class}**")
