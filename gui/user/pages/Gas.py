# Gas dashboard for the application
# date: 2024 - 06 - 15
# version: 0.0
# path: gui/user/page1/gas.py

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

import sys
import streamlit as st


sys.path.append("../../projects/CATY_Management/")
from core.settings import *
# Variables


st.header("Gas")
st.title("HHL Energy Consumption Analysis Tool (CATY)")
st.write("Graphics for Gas consumption. HHL Energy Consumption Analysis Tool (CATY)")

st.header("Gas Daily")
st.line_chart(gas_daily_df["calc_cons"])
st.markdown("[Home](#home) | [Water](#water) | [Power](#power)")

st.header("Gas Monthly")
st.line_chart(gas_monthly_df["calc_cons"])
