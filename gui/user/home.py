# CATY_app - A web application for the CATY chatbot
# Path: gui/user/home.py
# Description: Home page for the user
# date: 2024-06-15
# version: 0.0.0
"""
Home page for the user
"""

# import libraries
from email import header
import streamlit as st

from core.gui_streamlit import sidebar_home
from core.settings import (
    gas_monthly_df,
    water_monthly_df,
    power_monthly_df
)
from core.data_manager import *

# set date as index
gas_monthly_df = gas_monthly_df.set_index("date", inplace=False)
water_monthly_df = water_monthly_df.set_index("date", inplace=False)
power_monthly_df = power_monthly_df.set_index("date", inplace=False)
PAGE_SITE = "Home"

# site header
st.set_page_config(
    page_title="CATY",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

# header_pages(PAGE_SITE)

st.header("Gas")
st.line_chart(gas_monthly_df["calc_cons"])

st.header("Water")
st.line_chart(water_monthly_df["calc_cons"])

st.header("Power")
st.line_chart(power_monthly_df["calc_cons"])

sidebar_home()
