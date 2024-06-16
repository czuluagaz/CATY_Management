# home dashboard for the application
# date: 2024 - 06 - 15
# version: 0.0
# path: gui/user/home.py

""" This is the home page of the application. 
    It displays the energy consumption data for the home.
    The data is displayed in the form of line charts.
    parameters:
    gas: pandas dataframe
    water: pandas dataframe
    power: pandas dataframe
    returns:
    None"""


# Import libraries

from math import e
import streamlit as st
import pandas as pd

from core.settings import *

# Variables


st.header("Home")
st.title("HHL Energy Consumption Analysis Tool (CATY)")
st.write("Home page of the application. HHL Energy Consumption Analysis Tool (CATY)")

st.header("Gas")
st.line_chart(gas_daily_df["calc_cons"])

st.header("Water")
st.line_chart(water_daily_df["calc_cons"])

st.header("Power")
st.line_chart(power_daily_df["calc_cons"])
