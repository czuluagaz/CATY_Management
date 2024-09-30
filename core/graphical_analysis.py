# Graphical analysis
# Core Development
# date: 2024-06-15
# version: 0.0.0
# Path: /core/graphics.py
"""
The script is responsible for the graphical analysis of the data.
Methods for grouping data, creating graphs, and other graphical 
analysis tools are implemented here.
"""

# Importing the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Import local libraries
# sys.path.append("../../projects/CATY_Management/")
# from core.settings import (
#     gas_daily_df,
#     gas_monthly_df,
#     water_daily_df,
#     water_monthly_df,
#     power_daily_df,
#     power_monthly_df,
# )

# Variables


# Methods
# Processing methods


# function to group by day, week, month, quarter, season and year the data
def group_data(data: pd.DataFrame) -> tuple:
    """
    This method groups the data by day, week, month, quarter, season and year.
    parameters:
    data: pd.DataFrame

    return: tuple
    """
    # Convert the date column to a datetime object
    data["date"] = pd.to_datetime(data["date"])
    # Group the data by day
    data_day = data.resample("D", on="date").sum()
    # Group the data by week
    data_week = data.resample("W", on="date").sum()
    # Group the data by month
    data_month = data.resample("M", on="date").sum()
    # Group the data by quarter
    data_quarter = data.resample("Q", on="date").sum()
    # Group the data by season
    data_season = data.resample("Q-FEB", on="date").sum()
    # Group the data by year
    data_year = data.resample("Y", on="date").sum()
    # Convert the date column to a datetime object
    data_day["date"] = data_day.index
    data_week["date"] = data_week.index
    data_month["date"] = data_month.index
    data_quarter["date"] = data_quarter.index
    data_season["date"] = data_season.index
    data_year["date"] = data_year.index
    # Return the data
    return data_day, data_week, data_month, data_quarter, data_season, data_year


# Function to process the data
def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    This method processes the data.
    parameters:
    data: pd.DataFrame

    return: pd.DataFrame
    """
    # copy the dataset
    data_proc = data.copy()
    print(data_proc.head())
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


# Methods to plot the data
# Function to plot the data by column
def plot_data_column(data, title: str, ylabel: str, xlabel: str, color: str) -> None:
    """
    This method plots the daily data.
    parameters:
    data: pd.DataFrame
    title: str
    ylabel: str
    xlabel: str
    color: str

    return: None
    """

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


# Function to plot the data by date and consumption
def plot_date_consumption(
    data, title: str, ylabel: str, xlabel: str, color: str
) -> None:
    """
    This method plots the daily data.
    parameters:
    data: pd.DataFrame
    title: str
    ylabel: str
    xlabel: str
    color: str

    return: None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data["date"], data["consumption"], color=color)
    plt.grid()
    plt.legend([title])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.tight_layout()
    plt.show()


# Function to plot the data by date, meter and consumption
def plot_date_meter_consumption(
    data: pd.DataFrame, title: str, ylabel: str, xlabel: str, color: str
) -> None:
    """
    This method plots the daily data.
    parameters:
    data: pd.DataFrame
    title: str
    ylabel: str
    xlabel: str
    color: str

    return: None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data["date"], data["calc_cons"], color=color)
    plt.grid()
    plt.legend([title])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.tight_layout()
    plt.show()


# Function to plot the data grouped by day, week, month, quarter, season and year
def plot_grouped_data(
    data_day: pd.DataFrame,
    data_week: pd.DataFrame,
    data_month: pd.DataFrame,
    data_quarter: pd.DataFrame,
    data_season: pd.DataFrame,
    data_year: pd.DataFrame,
    title: str,
    ylabel: str,
    xlabel: str,
    color: str,
) -> None:
    """
    This method plots the daily data.
    parameters:
    data_day: pd.DataFrame
    data_week: pd.DataFrame
    data_month: pd.DataFrame
    data_quarter: pd.DataFrame
    data_season: pd.DataFrame
    data_year: pd.DataFrame
    title: str
    ylabel: str

    return: None
    """
    plt.figure(figsize=(10, 6))
    # plt.plot(data_day, color=color, label="Day")
    # plt.plot(data_week, color=color, label="Week")
    plt.plot(
        data_month,
        color="orange",
        label="Month",
        # marker="o",
        # markersize=5,
        # linestyle="--",
        linewidth=2,
        alpha=0.7,
        markerfacecolor="red",
        markeredgewidth=2,
        markeredgecolor="black",
        markevery=2,
        zorder=2,
        clip_on=True,
        solid_capstyle="round",
        dash_capstyle="round",
        dash_joinstyle="round",
        solid_joinstyle="round",
        antialiased=True,
        pickradius=5,
        snap=True,
        rasterized=True,
        path_effects=None,
        sketch_params=None,
    )
    # plt.plot(data_quarter, color=color, label="Quarter")
    # plot data by season showing winter, spring, summer and autumn with different colors
    plt.plot(
        data_season,
        color=color,
        label="Season",
        marker="o",
        markersize=5,
        linestyle="--",
        linewidth=2,
        alpha=0.7,
        markerfacecolor="red",
        markeredgewidth=2,
        markeredgecolor="black",
        markevery=2,
        zorder=2,
        clip_on=True,
        solid_capstyle="round",
        dash_capstyle="round",
        dash_joinstyle="round",
        solid_joinstyle="round",
        antialiased=True,
        pickradius=5,
        snap=True,
        rasterized=True,
        path_effects=None,
        sketch_params=None,
    )
    plt.plot(data_year, color=color, label="Year")
    #    # moving average
    #     plt.plot(data_year.rolling(window=30).mean(), color="black", linestyle="--")
    #     # trend line
    #     plt.plot(data_year.index, np.poly1d(np.polyfit(data_year.index, data_year, 1))(data_year.index))
    # color each season
    # plt.fill_between(
    #     data_season.index,
    #     data_season["calc_cons"],
    #     color="blue",
    #     alpha=0.1,
    #     label="Winter",
    # )
    # plt.fill_between(
    #     data_season.index,
    #     data_season["calc_cons"],
    #     color="green",
    #     alpha=0.1,
    #     label="Spring",
    # )
    # plt.fill_between(
    #     data_season.index,
    #     data_season["calc_cons"],
    #     color="red",
    #     alpha=0.1,
    #     label="Summer",
    # )
    # plt.fill_between(
    #     data_season.index,
    #     data_season["calc_cons"],
    #     color="orange",
    #     alpha=0.1,
    #     label="Autumn",
    # )
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend()
    plt.show()
