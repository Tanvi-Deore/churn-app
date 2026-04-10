import streamlit as st
from model import predict
from database import insert_data

st.title("Customer Churn Prediction")

customerID = st.text_input("Customer ID")
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.number_input("Tenure")
MonthlyCharges = st.number_input("Monthly Charges")

if st.button("Predict"):

    input_data = {
        "gender": gender,
        "tenure": tenure,
        "MonthlyCharges": MonthlyCharges
    }

    result = predict(input_data)

    insert_data(customerID, result)

    st.success(f"Prediction: {result}")