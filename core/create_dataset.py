# Preprocess raw data and create independent csv files for each utility
# Version: 1.0
# Author: CZU
# Date: 2023-12-01
"""
This script reads the raw data from the utilities and preprocesses it to
create independent csv files for each utility.
Parameters: 
    - raw_data.csv: raw data from utilities
    - water.csv: water utility data
    - power.csv: power utility data
    - gas.csv: gas utility data
    Returns:
    - water.csv: water utility data
    - power.csv: power utility data
    - gas.csv: gas utility data   
"""

# Importing required libraries
import time
import pandas as pd


# Initialize the timer
start = time.time()

# Variables
# call dataframe from tsv file in hard drive
DATASET = "data_storage/raw_data.csv"

# Read the csv file
df = pd.read_csv(DATASET, sep=",", encoding="utf-8", decimal=".")

# convert date to datetime
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")
df["date_eom"] = df["date"] + pd.offsets.MonthEnd(1)

# in headers change ' ' to '_'
df.columns = df.columns.str.replace(" ", "_")

# create a new df (dfref) with a column that contains dates
# from 31/01/2011 to 31/12/2024
dfref = pd.DataFrame(
    pd.date_range(start="30/06/2011", end="31/12/2024", freq="ME"), columns=["date_eom"]
)

# merge df and dfref in date_eom
df = pd.merge(dfref, df, on="date_eom", how="left")

# generate 3 csv files (water, power, gas) with the columns
df_water = df[
    [
        "date_eom",
        "date",
        "days",
        "w_id_meter",
        "water_m3",
        "w_cons",
        "w_av_day",
    ]
]
df_water.to_csv("data_storage/water.csv", index=False)

df_power = df[
    [
        "date_eom",
        "date",
        "days",
        "p_id_meter",
        "power_kwh",
        "p_cons",
        "p_av_day",
    ]
]
df_power.to_csv("data_storage/power.csv", index=False)

df_gas = df[
    [
        "date_eom",
        "date",
        "days",
        "g_id_meter",
        "gas_m3",
        "g_cons",
        "g_av_day",
    ]
]
df_gas.to_csv("data_storage/gas.csv", index=False)

# Print the execution time
print("Process finished. Execution time:", round(time.time() - start, 2), "seconds")
