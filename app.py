import streamlit as st
import joblib
import numpy as np

# Load your model
model = joblib.load('model.pkl')

st.title("Customer Churn Prediction")


print(type(model))



credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
balance = st.number_input("Balance", min_value=0.0, value=50000.0)
estimated_salary = st.number_input("Estimated Salary (in ₹)", min_value=0.0, value=70000.0)
is_active_member = st.selectbox("Is Active Member?", ["Yes", "No"])
is_active_member_encoded = 1 if is_active_member == "Yes" else 0  

gender = st.selectbox("Gender", ["Male", "Female"])
gender_encoded = 0 if gender == "Male" else 1  

geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
geography_encoded = {"France": 0, "Spain": 1, "Germany": 2}[geography] 

if st.button("Predict"):

    features = np.array([[credit_score, age, balance, estimated_salary, is_active_member_encoded, gender_encoded, geography_encoded]])
    

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Customer will exit!")
    else:
        st.success("Customer will stay!")
