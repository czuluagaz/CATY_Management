# Preprocess raw data and create independent csv files for each utility
# Version: 1.0
# Author: CZU
# Date: 2023-12-01

# Importing required libraries
import time
import pandas as pd


# Initialize the timer
start = time.time()

# Variables
# call dataframe from tsv file in hard drive
dataset = "data_storage/raw_data.csv"

# Read the csv file
df = pd.read_csv(dataset, sep=",", encoding="utf-8", decimal=".")

# # drop columns 6 and 7
# df.drop(df.columns[[1, 6, 7]], axis=1, inplace=True)

# convert date to datetime
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")
df["date_eom"] = df["date"] + pd.offsets.MonthEnd(1)

# in headers change ' ' to '_'
df.columns = df.columns.str.replace(" ", "_")

# # rename columns 7, 8, 11 as 'cons', 'av_day.1', 'av_day.2' respectively
# df.rename(
#     columns={
#         df.columns[6]: "cons",
#         df.columns[7]: "av_day.1",
#         df.columns[10]: "av_day.2",
#     },
#     inplace=True,
# )

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
        "gas_m3",
        "g_cons",
        "g_av_day",
    ]
]
df_gas.to_csv("data_storage/gas.csv", index=False)

# Print the execution time
print(
    "Process finished. Execution time:", round(time.time() - start, 2),
    "seconds"
)
