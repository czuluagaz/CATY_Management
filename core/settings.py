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

# import sys
# import logging

from core.data_manager import csv_to_dataframe


# C:\Users\zudel\projects\CATY_Management\data_storage\resampled_data_D_gas.csv
# Paths
path = "../../projects/CATY_Management/"
# gas
gas_daily_path = os.path.join(path, "data_storage", "resampled_data_D_gas.csv")
gas_monthly_path = os.path.join(path, "data_storage", "grouped_data_month_gas.csv")

# electricity
electricity_daily_path = os.path.join(
    path, "data_storage", "resampled_data_D_power.csv"
)
electricity_monthly_path = os.path.join(
    path, "data_storage", "grouped_data_month_power.csv"
)

# water
water_daily_path = os.path.join(path, "data_storage", "resampled_data_D_water.csv")
water_monthly_path = os.path.join(path, "data_storage", "grouped_data_month_water.csv")


# Dataframes

gas_daliy_df = csv_to_dataframe(gas_daily_path)
gas_monthly_df = csv_to_dataframe(gas_monthly_path)
water_daily_df = csv_to_dataframe(water_daily_path)
water_monthly_df = csv_to_dataframe(water_monthly_path)

print(gas_daliy_df.head())
