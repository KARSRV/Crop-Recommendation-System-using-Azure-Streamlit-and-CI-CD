# streamlit_app.py
import streamlit as st
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load('crop_rf_model.pkl')
scaler = joblib.load('scaler.pkl')

# Streamlit UI
st.title("Crop Recommendation System")

st.markdown("Enter soil and weather conditions to get the best crop suggestion.")

# Input fields
N = st.number_input('Nitrogen (N)', min_value=0)
P = st.number_input('Phosphorus (P)', min_value=0)
K = st.number_input('Potassium (K)', min_value=0)
temperature = st.number_input('Temperature (°C)', format="%.2f")
humidity = st.number_input('Humidity (%)', format="%.2f")
ph = st.number_input('Soil pH', format="%.2f")
rainfall = st.number_input('Rainfall (mm)', format="%.2f")

if st.button("Predict Crop"):
    # Create input DataFrame
    input_df = pd.DataFrame([{
        'N': N,
        'P': P,
        'K': K,
        'temperature': temperature,
        'humidity': humidity,
        'ph': ph,
        'rainfall': rainfall
    }])

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)[0]

    # Show result
    st.success(f"Recommended Crop: **{prediction}**")
