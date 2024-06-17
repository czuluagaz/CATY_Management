# CATY_app - A web application for the CATY chatbot
# Path: gui/user/home.py
# Description: Home page for the user
# date: 2024-06-15
# version: 0.0.0
"""
Home page for the user
"""

# import libraries
import streamlit as st

from core.settings import (
    gas_monthly_df,
    water_monthly_df,
    power_monthly_df,
)

st.title("CATY- Consumption Analysis Tool Yield")
st.header("Home")
st.title("HHL Energy Consumption Analysis Tool (CATY)")
st.write("Home page of the application. HHL Energy Consumption Analysis Tool (CATY)")

st.header("Gas")
st.line_chart(gas_monthly_df["calc_cons"])

st.header("Water")
st.line_chart(water_monthly_df["calc_cons"])

st.header("Power")
st.line_chart(power_monthly_df["calc_cons"])
