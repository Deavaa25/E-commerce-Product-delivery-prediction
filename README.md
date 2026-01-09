# E-commerce-Product-delivery-prediction
A machine learning project that predicts whether an e-commerce product will be delivered on time based on order, customer, and product features. Includes data preprocessing, model training, evaluation, and deployment-ready insights.

## Project Overview
This project predicts whether a product will be delivered **on time or delayed** using machine learning models.

## Problem Statement
Late deliveries negatively impact customer satisfaction.  
This system helps predict delivery outcomes in advance using historical data.

## Dataset
The dataset contains:
- Product weight
- Product importance
- Discount offered
- Customer calls
- Warehouse & shipment details

## Machine Learning Models Used
- Logistic Regression
- Decision Tree
- Random Forest (Best Accuracy)
- XGBoost

## Results
- Random Forest achieved the highest accuracy
- Heavier products showed better on-time delivery
- Frequent customer calls indicated delays

## Web Application
Built using **Streamlit** for real-time prediction.

## How to Run the Project
```bash
pip install -r requirements.txt
streamlit run app.py

## Model File
The trained model file (`Final_Project_pdp.pkl`) is not included in this repository due to GitHub file size limits.
You can generate the model by running:

Product Delivery Prediction.ipynb


Download trained model:
https://drive.google.com/file/d/1uBoMqLReNsblmFggDgJgFNaWqUoD-1gi/view?usp=drive_link
