# 🏠 House Price Prediction Project

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python) ![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-orange?logo=scikit-learn) ![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit)

This project focuses on building a machine learning model to predict the price of individual houses based on a variety of their features. The project includes data cleaning, feature engineering, model training, and an interactive web application built with Streamlit.

---

## 📋 Project Overview

The primary goal is to accurately predict house prices using tangible features like area, number of bedrooms, and amenities. Unlike models based on aggregated neighborhood data, this project provides predictions for single properties, making the results more intuitive and practical.

### Dataset

The model is trained on a dataset containing information for 545 individual houses. Key features include:
* **Numerical:** `price`, `area`, `bedrooms`, `bathrooms`, `stories`, `parking`
* **Categorical:** `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`, `furnishingstatus`

---

## 🛠️ Methodology

The project was executed in three main stages:

### 1. Data Cleaning
The raw data contained several categorical (text-based) columns. These were converted into a numerical format that the model could understand:
* **Binary Features:** Columns with 'yes'/'no' values (e.g., `mainroad`, `guestroom`) were mapped to `1` and `0`.
* **Multi-Category Features:** The `furnishingstatus` column was converted into numerical columns using one-hot encoding.

### 2. Feature Engineering
To provide the model with more insightful data, two new features were created:
* `area_per_bedroom`: The ratio of the total area to the number of bedrooms, indicating spaciousness.
* `bath_bed_ratio`: The ratio of bathrooms to bedrooms, often a marker for modern or premium properties.

### 3. Model Training
A **Random Forest Regressor** was chosen for its high accuracy and robustness. The data was split into an 80% training set and a 20% testing set to ensure the model's performance was evaluated on unseen data.

---

## 📊 Results

The trained model was evaluated on the test set to measure its predictive accuracy.

* **R-squared (R²) Score:** **0.61**

This score indicates that the model can explain approximately 61% of the variability in house prices based on the provided features.

---

## 🚀 Interactive Web App

An interactive web application was built using **Streamlit** to allow for easy, real-time predictions. Users can input a house's features into a simple sidebar interface and instantly receive a price prediction.


*(You can add a screenshot of your app here and name it `app_screenshot.png`)*

### How to Run the App Locally
1.  Make sure you have Python and the required libraries installed (`streamlit`, `pandas`, `scikit-learn`, `joblib`).
2.  Open your terminal or command prompt and navigate to the project folder.
3.  Run the following command:
    ```bash
    streamlit run app.py
    ```
4.  The application will open automatically in your web browser.

---

## 

* **MD.GOLAM RABBANI**
* **2203059**
