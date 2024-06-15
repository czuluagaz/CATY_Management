# Import libraries

import streamlit as st
import pandas as pd

# Variables
gas = pd.read_csv("data_storage/resampled_data_D_gas.csv")
water = pd.read_csv("data_storage/resampled_data_D_water.csv")
power = pd.read_csv("data_storage/resampled_data_D_power.csv")

st.header('Home')
st.title('HHL Energy Consumption Analysis Tool (CATY)')
st.write('Home page of the application. HHL Energy Consumption Analysis Tool (CATY)')

#df = pd.read_csv(r'/home/cyat/projects/CATY_Management/data_storage/resampled_data_D_gas.csv')
st.header("Gas")
st.line_chart(gas['calc_cons'])

st.header("Water")
st.line_chart(water['calc_cons'])

st.header("Power")
st.line_chart(power['calc_cons'])