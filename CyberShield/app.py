import streamlit as st
import pandas as pd
import joblib

model = joblib.load("cybershield_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.set_page_config(page_title="CyberShield IDS", layout="wide")

st.title("CyberShield: AI-Based Intrusion Detection System")
st.write("This app predicts whether network traffic is normal or malicious.")

st.subheader("Enter Network Traffic Feature Values")

input_data = {}

for col in feature_columns:
    input_data[col] = st.number_input(col, value=0.0)

if st.button("Predict"):
    df_input = pd.DataFrame([input_data])
    df_scaled = scaler.transform(df_input)
    prediction = model.predict(df_scaled)[0]

    if prediction == 0:
        st.success("Prediction: Normal Traffic")
    else:
        st.error("Prediction: Attack Traffic Detected")