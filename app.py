import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('vehicles_us.csv')

# Header
st.header('🚗 US Vehicle Sales Dashboard')

# Checkbox to filter out extremely high-priced listings
if st.checkbox('Hide Listings Above $100,000'):
    df = df[df['price'] < 100000]

# Histogram
st.subheader('Price Distribution')
fig1 = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig1)

# Scatter plot
st.subheader('Price vs. Odometer')
fig2 = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer')
st.plotly_chart(fig2)