# gui_streamlit.py


# import libraries
from email import header
import re
import streamlit as st
import pandas as pd

# method to create header and title
def header_pages(page):
    menu = st.markdown("[Home](#home) | [Water](#water) | [Power](#power)")
    title_app = st.title("CATY- Consumption Analysis Tool Yield")
    header_page = st.header(f"{page}")
    subheader_page = st.subheader("HHL Energy Consumption Analysis Tool (CATY)")
    return menu, title_app, header_page, subheader_page

# method to create the sidebar
def sidebar_home():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Data Analysis", "Data Visualization", "Data Prediction"])
    return page

# method to graph daily data
def graph_daily_data(df, page):
    st.header(f"{page} Daily")
    st.line_chart(df["calc_cons"])
    return None

# method to graph monthly data
def graph_monthly_data(df, page):
    st.header(f"{page} Monthly")
    st.line_chart(df["calc_cons"])
    return None
