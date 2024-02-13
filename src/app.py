import streamlit as st
import pickle
import numpy as np

# Load your trained model
model_path = '../Models/bitcoin_price_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit webpage layout
st.title('Bitcoin Price Prediction')

# Creating input fields for the features
open_price = st.number_input('Open Price', value=0.0, format="%.2f")
high = st.number_input('High Price', value=0.0, format="%.2f")
low = st.number_input('Low Price', value=0.0, format="%.2f")
price_lag1 = st.number_input('Price Lag 1', value=0.0, format="%.2f")
price_7day_rolling_mean = st.number_input('Price 7-Day Rolling Mean',
                                          value=0.0, format="%.2f")

# Button to make prediction
if st.button('Predict'):
    # Prepare the feature array for prediction
    features = np.array(
        [[open_price, high, low, price_lag1, price_7day_rolling_mean]])

    # Make prediction
    prediction = model.predict(features)

    # Display the prediction
    st.write(f'Predicted Bitcoin Price: ${prediction[0]:,.2f}')

