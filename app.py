import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import ui  

# Apply UI styles
ui.apply_custom_styles()
ui.show_header()

# Load the model once
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("cifar100_model.keras")

model = load_model()

# CIFAR-10 class labels
class_names = ["airplane", "automobile", "bird", "cat", "deer",
               "dog", "frog", "horse", "ship", "truck"]

# File Uploader
uploaded_file = st.file_uploader("📂 Upload an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Convert file to image
    image = Image.open(uploaded_file)

    # Display uploaded image
    st.image(image, caption="🖼️ Uploaded Image", use_container_width=True)

    # Classification button
    if st.button("🔍 Classify Image", key="classify_button"):
        # Preprocess image
        image = image.resize((32, 32))  # Resize to CIFAR-10 dimensions
        image_array = np.array(image).astype("float32") / 255.0  # Normalize
        batch_image = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Predict class
        predictions = model.predict(batch_image)
        predicted_class_index = np.argmax(predictions[0])
        predicted_class_name = class_names[predicted_class_index]
        confidence = np.max(predictions[0])

        # Display results
        st.markdown(f'<h2 style="color:#000000;">Prediction: {predicted_class_name}</h2>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size:18px; color:#B0B0B0;">Confidence: {confidence:.4f}</p>', unsafe_allow_html=True)
