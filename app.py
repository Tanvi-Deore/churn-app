import streamlit as st
from model import predict
from database import insert_data
from database import fetch_data
import pandas as pd

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

st.subheader("📊 Dashboard")

data = fetch_data()

if data:
    df = pd.DataFrame(data, columns=["id", "customerID", "prediction"])

    st.write("All Records:")
    st.dataframe(df)
else:
    st.write("No data found")

df["prediction_label"] = df["prediction"].map({0: "No", 1: "Yes"})

st.bar_chart(df["prediction_label"].value_counts())