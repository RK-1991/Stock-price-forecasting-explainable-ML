
# Explainable Stock Price Forecasting using Time-Series ML

## 📌 Project Overview
This project builds a machine learning model to forecast stock prices using historical financial data and explains model predictions using explainable AI techniques.

The goal is not just prediction accuracy, but interpretability — understanding *why* a model predicts a certain price movement.

## 🏦 Business Use Case
- Investment decision support
- Risk analysis
- Market trend understanding
- Financial forecasting with transparency

## 🧠 Approach
1. Collect historical stock price data
2. Perform feature engineering using technical indicators
3. Train time-series machine learning models
4. Evaluate forecasting performance
5. Explain predictions using SHAP values

## 📊 Models Used
- Baseline forecasting
- Machine Learning regression models
- Explainable AI (SHAP)
- ## Deep Learning: LSTM Model
- Model predicts stock prices using sequences of past prices (10-day window)
- Architecture: 1 LSTM layer (50 units) + Dense output
- Evaluated using RMSE and MAE
- Visuals: Plot comparing actual vs predicted prices


## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- SHAP
- Yahoo Finance API
- Matplotlib / Plotly

## 📁 Project Structure
## Interactive Streamlit App

- Predict stock prices interactively
- Users can select stock symbol and date range
- Visualizes historical stock prices
- Run locally with:
  ```bash
  pip install -r requirements.txt
  streamlit run app/app.py

