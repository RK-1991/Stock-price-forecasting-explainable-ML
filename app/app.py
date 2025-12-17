import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

st.title("Stock Price Predictor")

# User inputs
symbol = st.text_input("Enter Stock Symbol", "AAPL")
start = st.date_input("Start Date", pd.to_datetime("2022-01-01"))
end = st.date_input("End Date", pd.to_datetime("2025-12-16"))

# Download data
data = yf.download(symbol, start=start, end=end)

# Show table
st.write("Historical Data")
st.dataframe(data.tail())

# Plot Close price
st.line_chart(data['Close'])
