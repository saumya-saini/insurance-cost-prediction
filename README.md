Insurance Cost Prediction

Problem Statement

This project predicts health insurance premium prices using demographic and medical attributes. The goal is to identify key risk factors influencing insurance pricing and build a machine learning model to estimate premiums.


Target Variable

The target variable for this project is:

PremiumPrice

This represents the predicted insurance premium cost for an individual.

Target Variable

PremiumPrice

Project Steps

Exploratory Data Analysis (EDA)

Hypothesis Testing

Feature Engineering (BMI)

Machine Learning Modeling

Model Deployment using Streamlit

Models Used

Linear Regression

R² ≈ 0.71

Random Forest Regressor

R² ≈ 0.875

Random Forest produced significantly better predictions.

Key Insights

Age is the strongest predictor of premium price.

Chronic diseases increase premiums.

Number of major surgeries increases premiums.

BMI has a weak relationship with premium cost.

Deployment

A Streamlit web app was created to estimate insurance premiums based on user inputs.

Link:

https://insurance-cost-prediction-ah74qpprixx5ldc8zmmbxv.streamlit.app/


Technologies Used:

Python

Pandas

Scikit-learn

Streamlit

Tableau

Repository Structure:

insurance-cost-prediction/

insurance_cost_prediction.ipynb

app.py

model.pkl

requirements.txt

README.md
