# Graphical analysis
# Core Development
# date: 2024-06-15
# version: 0.0.0
# Path: /core/graphics.py
""" 
The script is responsible for the graphical analysis of the data.
Methods for grouping data, creating graphs, and other graphical analysis tools are implemented here.
"""

# Importing the necessary libraries
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Import local libraries
sys.path.append("../../projects/CATY_Management/")
from core.settings import (
    gas_daily_df,
    gas_monthly_df,
    water_daily_df,
    water_monthly_df,
    power_daily_df,
    power_monthly_df,
)

# Variables
gas_day = gas_daily_df
gas_month = gas_monthly_df
water_day = water_daily_df
water_month = water_monthly_df
power_day = power_daily_df
power_month = power_monthly_df

# Methods


# Function to process the data
def process_data(data):
    # copy the dataset
    data_proc = data.copy()
    # Convert the date column to a datetime object
    data_proc["date"] = pd.to_datetime(data_proc["date"])
    # Sort the data by date
    data_proc = data_proc.sort_values("date")
    # drop the duplicates rows
    data_proc = data_proc.drop_duplicates(subset="date")
    # # Drop the columns that are not needed
    # data_proc = data_proc.drop(columns=["days", "diff_cons", "days_month", "days_cons"])
    # # Convert the data to a numpy array
    # data = data.to_numpy()
    # Return the data
    return data_proc


# Function to plot the data by column
def plot_data_column(data, title: str, ylabel: str, xlabel: str, color: str) -> None:
    """
    This method plots the daily data.
    """
    # # Process the data
    # data = process_data(data)
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(data, color=color)
    plt.grid()
    # moving average
    plt.plot(data.rolling(window=30).mean(), color="black", linestyle="--")
    # trend line
    plt.plot(data.index, np.poly1d(np.polyfit(data.index, data, 1))(data.index))
    plt.legend([title, "30-Day Moving Average", "Trend Line"])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.tight_layout()
    plt.show()


plot_data_column(
    gas_day["calc_cons"], "Gas Daily Consumption", "Consumption (m3)", "Date", "blue"
)
