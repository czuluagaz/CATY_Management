# Preprocess raw data and create independent csv files for each utility
# Version: 1.0
# Author: CZU
# Date: 2023-12-01

# Importing required libraries
import csv
import os
import pandas as pd

# Variables
# call dataframe from tsv file in hard drive
dataset = 'data_storage/raw_data.csv'

# Read the csv file
df = pd.read_csv(dataset, decimal=',') # read the csv file and change ',' to '.'

# drop columns 6 and 7
df.drop(df.columns[[6, 7]], axis=1, inplace=True)


# format 'date' column to datetime
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')


df.describe()
print(df.info()) 



# # in the column 'date' add the lines for the missing months from 31/01/2011 to 31/01/2024
# df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
# df = df.set_index('date').resample('M').asfreq().reset_index()

# # fill the missing values with the previous value
# df = df.fillna(method='ffill')


# # create a column with (chrono_date) that contains the dates starting 31/01/2019 to 31/12/202024
# df['chrono_date'] = pd.date_range(start='31/01/2019', end='31/12/2024', freq='Month')

# # create 3 new dataframes (water, power, gas), define the columns for each dataframe and save them as csv files
# df_water = df[['Date', 'Time', 'Water']]
# df_water.to_csv('data_storage/water.csv', index=False)

# df_power = df[['Date', 'Time', 'Power']]
# df_power.to_csv('data_storage/power.csv', index=False)

# df_gas = df[['Date', 'Time', 'Gas']]
# df_gas.to_csv('data_storage/gas.csv', index=False)


print(df.head(5))


