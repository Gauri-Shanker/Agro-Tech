import streamlit as st
import tensorflow as tf
import numpy as np
import json
from PIL import Image

# -----------------------------
# Load Class Indices (FIXED)
# -----------------------------
@st.cache_resource
def load_class_indices():
    with open("class_indices.json", "r") as f:
        raw = json.load(f)
    
    # Convert from {"label": index} → {index: "label"}
    fixed = {int(v): k for k, v in raw.items()}
    return fixed

class_indices = load_class_indices()

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("best_model.h5")

model = load_model()

# -----------------------------
# Preprocess Function
# -----------------------------
def preprocess_image(img):
    img = img.convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# -----------------------------
# Prediction Function
# -----------------------------
def predict_disease(img, threshold=0.60):

    processed = preprocess_image(img)
    preds = model.predict(processed)
    
    max_prob = np.max(preds)
    index = np.argmax(preds)

    if max_prob < threshold:
        return "❌ Not a leaf or Uncertain image", max_prob
    
    return class_indices[index], max_prob


# -----------------------------
# Streamlit App
# -----------------------------
st.title("🌿 Plant Disease Classifier")

uploaded = st.file_uploader("Upload leaf image", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Image", width=300)

    label, conf = predict_disease(img)

    if "❌" in label:
        st.error("This image does not appear to be a plant leaf.")
    else:
        st.success(f"Disease: {label}\nConfidence: {conf:.2f}")

