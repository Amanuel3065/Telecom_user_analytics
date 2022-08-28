import os, sys
import streamlit as st

sys.path.insert(0, './dashboard')

from multiapp import MultiApp
from applications import sat_calculator, user_engagement, experience_analysis, satisfaction_analysis

st.set_page_config(page_title="Telecom User Data Visualization", layout="wide")

app = MultiApp()

st.sidebar.markdown("""
# Telecom User Data Analysis""")

# Add all your application here
app.add_app("user_engagement", user_engagement.app)
app.add_app("experience_analysis", experience_analysis.app)
app.add_app("satisfaction_analysis", satisfaction_analysis.app)
app.add_app("satisfaction_calculator", sat_calculator.app)

# The main app
app.run()
