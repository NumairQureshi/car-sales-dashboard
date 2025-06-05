# car-sales-dashboard
car-sales-dashboard

## Live App

You can view the live dashboard here:  
👉 [https://car-sales-dashboard-qqf9.onrender.com](https://car-sales-dashboard-qqf9.onrender.com)

## US Car Sales Dashboard – EDA to Deployment

## Project Overview

This project walks through the full data science pipeline — from Exploratory Data Analysis (EDA) in Jupyter Notebook, to building a dashboard in Streamlit, and finally deploying it live on Render.

It was built as part of a TripleTen Data Science milestone project and demonstrates real-world skills in EDA, dashboarding, and deployment.

## Project Goals
	•	Analyze US vehicle sales data to extract insights
	•	Identify trends in price, manufacturer, and model year
	•	Visualize these insights with an interactive dashboard
	•	Deploy the dashboard so it’s publicly accessible online

## Repository Contents
- EDA.ipynb - Jupyter Notebook with full exploratory analysis and markdown commentary
- app.py - Streamlit app that turns EDA insights into an interactive dashboard
- requirements.txt - Python dependencies required to run the app
- .streamlit/config.toml - Config file for Streamlit deployment
- vehicles_us.csv - Original dataset

## Live Dashboard
You can explore the fully deployed dashboard here: https://car-sales-dashboard-qqf9.onrender.com
- Please let me know if it fails to load.  I had to manually deploy it twice. I think there is an issue because I use the free tier on Render, which may have limitations.

## Key Takeaways
	•	Gained hands-on experience connecting Jupyter and Streamlit
	•	Learned to manage project environments using Terminal
	•	Navigated real-world deployment challenges using Render
	•	Strengthened understanding of vehicle pricing patterns

 ## How to Run Locally

Follow these steps to run this app on your own machine:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/NumairQureshi/car-sales-dashboard.git
   cd car-sales-dashboard

2. **Create and activate a virtual environment (on Mac/Linux) using Terminal:
python3 -m venv venv
source venv/bin/activate

If using Windows, then you do this:
python -m venv venv
venv\Scripts\activate

3. **Install required packages**
pip install -r requirements.txt

4. **run Streamlit**
streamlit run app.py
