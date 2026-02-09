import streamlit as st
import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Insurance Premium Predictor")

age = st.slider("Age", 18, 66, 30)
diabetes = st.selectbox("Diabetes", [0, 1])
bp = st.selectbox("Blood Pressure Problems", [0, 1])
transplant = st.selectbox("Any Transplants", [0, 1])
chronic = st.selectbox("Chronic Diseases", [0, 1])
height = st.slider("Height (cm)", 145, 188, 165)
weight = st.slider("Weight (kg)", 51, 132, 70)
allergies = st.selectbox("Known Allergies", [0, 1])
cancer = st.selectbox("Family Cancer History", [0, 1])
surgeries = st.slider("Number of Major Surgeries", 0, 3, 0)

bmi = weight / ((height / 100) ** 2)

features = np.array([[age, diabetes, bp, transplant, chronic,
                      height, weight, allergies, cancer,
                      surgeries, bmi]])

if st.button("Predict Premium"):
    prediction = model.predict(features)
    st.success(f"Estimated Premium: {int(prediction[0])}")