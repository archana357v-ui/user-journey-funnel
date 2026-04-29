import streamlit as st
import pickle
import numpy as np

st.title("User Journey Prediction App")

# Load model
try:
    model = pickle.load(open("random_forest_model.pkl", "rb"))
    st.success("Model loaded successfully ✅")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Inputs
age = st.number_input("Age", 0, 100, 25)
income = st.number_input("Income", 0, 1000000, 50000)
time_spent = st.number_input("Time Spent (minutes)", 0, 500, 30)
pages = st.number_input("Pages Visited", 0, 50, 5)

# Prediction
if st.button("Predict"):
    data = np.array([[age, income, time_spent, pages]])
    
    prediction = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1]

    if prediction == 1:
        st.success(f"Will Convert ✅ ({prob*100:.2f}%)")
    else:
        st.error(f"Will NOT Convert ❌ ({prob*100:.2f}%)")