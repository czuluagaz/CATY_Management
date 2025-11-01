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

from email import header
import streamlit as st


from core.settings import (power_daily_df, power_monthly_df)
from core.gui_streamlit import *

# Variables
# for each df, set date as index
power_daily_df.set_index("date", inplace=False)
power_monthly_df.set_index("date", inplace=False)
page = "Electricity"

# header_pages(page)
st.markdown("[Home](#home) | [Water](#water) | [Power](#power)")
st.title("CATY- Consumption Analysis Tool Yield")
st.header(f"{page}")
st.subheader("HHL Energy Consumption Analysis Tool (CATY)")




st.header("Electricity Daily")
st.line_chart(power_daily_df["calc_cons"])
st.markdown("[Home](#home) | [Water](#water) | [Power](#power)")

st.header("Electricity Monthly")
st.line_chart(power_monthly_df["calc_cons"])
