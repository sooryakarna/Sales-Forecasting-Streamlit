import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Sales Forecasting", layout="wide")

st.markdown("<h1 style='text-align:center;color:#2196F3;'>📊 Sales Forecasting</h1>", unsafe_allow_html=True)

# Sample sales data
months = np.arange(1,13)
sales = np.array([200,220,250,270,300,320,350,370,400,420,450,480])

df = pd.DataFrame({"Month":months,"Sales":sales})

# Train model
model = LinearRegression()
model.fit(df[["Month"]], df["Sales"])

# Plot
fig, ax = plt.subplots()
ax.plot(months, sales)
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
st.pyplot(fig)

future_month = st.number_input("Enter Future Month", min_value=1)

if st.button("Predict"):
    prediction = model.predict([[future_month]])
    st.success(f"Predicted Sales: {prediction[0]:.2f}")




REQUIREMENT.TXT
streamlit
pandas
numpy
scikit-learn
matplotlib
