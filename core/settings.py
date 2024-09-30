# Config
# Core Config
# version 0.0
# Date: 202-06-15


"""
This is the core configuration file for the project.
All the configuration variables are defined here.
"""


# Importing the required libraries
import os
# sys.path.append("../../projects/CATY_Management/")
import pandas as pd
import seaborn as sns
# import sys
# import logging


# C:\Users\zudel\projects\CATY_Management\data_storage\resampled_data_D_gas.csv
# Paths
PATH = "../../projects/CATY_Management/"
# gas
gas_daily_path = os.path.join(PATH, "data_storage", "resampled_data_D_gas.csv")
gas_monthly_path = os.path.join(
    PATH, "data_storage", "grouped_data_month_gas.csv"
)

# electricity
electricity_daily_path = os.path.join(
    PATH, "data_storage", "resampled_data_D_power.csv"
)
electricity_monthly_path = os.path.join(
    PATH, "data_storage", "grouped_data_month_power.csv"
)

# water
water_daily_path = os.path.join(
    PATH, "data_storage", "resampled_data_D_water.csv"
)
water_monthly_path = os.path.join(
    PATH, "data_storage", "grouped_data_month_water.csv"
)
# path to db
db_path = os.path.join(PATH, "DB", "caty_sql")

# Dataframes

gas_daily_df = pd.read_csv(gas_daily_path)
gas_monthly_df = pd.read_csv(gas_monthly_path)
water_daily_df = pd.read_csv(water_daily_path)
water_monthly_df = pd.read_csv(water_monthly_path)
power_daily_df = pd.read_csv(electricity_daily_path)
power_monthly_df = pd.read_csv(electricity_monthly_path)
print("Dataframes loaded successfully!")

# Color palette for the plots with seaborn and matplotlib
gas_color_palette = sns.color_palette("coolwarm", 7)
water_color_palette = sns.color_palette("coolwarm", 6)
power_color_palette = sns.color_palette("coolwarm", 5)

# Ressources path
icon_path = os.path.join(
    PATH, "ressources", "images", "utilities-energy-monitor.svg"
)
