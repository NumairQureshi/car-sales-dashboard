import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('vehicles_us.csv')
# Sidebar filter for model year
min_year = int(df['model_year'].min())
max_year = int(df['model_year'].max())
selected_year = st.sidebar.slider('Select Model Year', min_year, max_year, (min_year, max_year))
df = df[(df['model_year'] >= selected_year[0]) & (df['model_year'] <= selected_year[1])]

# Header
st.header('🚗 US Vehicle Sales Dashboard')

# Slider to filter price range
st.subheader('Select Price Range')
min_price = int(df['price'].min())
max_price = int(df['price'].max())
price_range = st.slider(
    "Choose the price range:",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price)
)

# Filter data using slider
filtered_df = df[df['price'].between(*price_range)]

# Histogram
st.subheader('Price Distribution')
fig1 = px.histogram(filtered_df, x='price', title='Price Distribution')
st.plotly_chart(fig1)

# Scatter plot
st.subheader('Price vs. Odometer')
fig2 = px.scatter(filtered_df, x='odometer', y='price', title='Price vs. Odometer')
st.plotly_chart(fig2)

# Optional: Show raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw Data Preview')
    n_rows = st.slider('Number of rows to view:', 5, 100, 5)
    st.dataframe(filtered_df.head(n_rows))