import streamlit as st
import pandas as pd
import numpy as np
import pickle

# st.header("Product Delivery Prediction")
st.set_page_config(
    page_title="Product Delivery Predictor",
    page_icon="🚚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# st.write("PLEASE! ENTER THE DETAILS TO KNOW ABOUT THE PRODUCT DELIVERY STATUS.")
st.markdown("## 🚚 Product Delivery Prediction")
st.markdown("Predict whether your order will arrive **on time** ⏱️")

# Load trained model
with open('Final_Project_pdp.pkl', 'rb') as f:
    model = pickle.load(f)
with open("feature_names.pkl", "rb") as f:
    feature_names = pickle.load(f)
# User Inputs
Warehouse_block = st.selectbox("Warehouse Block", ['A', 'B', 'C', 'D', 'F'])
Mode_of_Shipment = st.selectbox("Mode of Shipment", ['Flight', 'Road', 'Ship'])
Customer_care_calls = st.slider("Customer care calls", min_value=0, max_value=10, step=1)
Customer_rating = st.slider("Customer rating", min_value=1, max_value=5, step=1)
Cost_of_the_Product = st.number_input("Cost of the product", 50.0, 5000.0, step=10.0)
Prior_purchases = st.number_input("Prior purchases", min_value=0)
Product_importance = st.selectbox("Product importance", ["low", "medium", "high"])
Product_importance = {'low': 1, 'medium': 2, 'high': 3}[Product_importance]
Gender = st.selectbox("Gender", ["Female", "Male"])
Gender = 1 if Gender == "Male" else 0
Discount_offered = st.number_input("Discount offered", 0.0, 75.0, step=1.0)
Weight_in_gms = st.number_input("Weight in grams", 50.0, 10000.0, step=10.0)
# Create input dataframe with exact training columns
input_df = pd.DataFrame(
    np.zeros((1, len(feature_names))),
    columns=feature_names
)
# Fill numerical & encoded values
input_df['Customer_care_calls'] = Customer_care_calls
input_df['Customer_rating'] = Customer_rating
input_df['Cost_of_the_Product'] = Cost_of_the_Product
input_df['Prior_purchases'] = Prior_purchases
input_df['Product_importance'] = Product_importance
input_df['Gender'] = Gender
input_df['Discount_offered'] = Discount_offered
input_df['Weight_in_gms'] = Weight_in_gms
#One-Hot Encoding
input_df[f'Warehouse_block_{Warehouse_block}'] = 1
input_df[f'Mode_of_Shipment_{Mode_of_Shipment}'] = 1
# Prediction
if st.button("Predict"):
    prediction = model.predict(input_df)

    if prediction[0] == 0:
        st.write("Product has reached on time")
    else:
        st.write("Product has NOT reached on time ")
