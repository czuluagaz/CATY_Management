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
df.drop(df.columns[[1, 6, 7]], axis=1, inplace=True)

# split column 'date' into 3 columns 'day', 'month', 'year'
df[['day', 'month', 'year']] = df['date'].str.split('/', expand=True)

# in column 'year' if year is YY change it to YYYY
df['year'] = df['year'].apply(lambda x: '20' + x if len(x) == 2 else x)

# merge columns 'day', 'month', 'year' into a new column 'date' format YYYY-MM-DD
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
df = df.drop(columns=['day', 'month', 'year'])

# create a column "date_eom" with the end of the month from the column 'date' 
df['date_eom'] = pd.to_datetime(df['date'], format='dd-mm-YYYY') + pd.offsets.MonthEnd(0)

# create a new df (dfref) with a column that contains dates from 31/01/2011 to 31/12/2024
dfref = pd.DataFrame(pd.date_range(start='31/01/2011', end='31/12/2024', freq='M'), columns=['date_eom'])

# merge df and dfref in date_eom
df = pd.merge(dfref, df, on='date_eom', how='left')

# drop from 'date_eom' dates before 1/06/2011
df = df[df['date_eom'] > '29/06/2011']

# generate 3 csv files (water, power, gas) with the columns 'date_eom', 'time', 'water', 'power', 'gas'
df_water = df[['date_eom', 'date', 'days', 'water m3', 'cons', 'av day.1']]
df_water.to_csv('data_storage/water.csv', index=False)

df_power = df[['date_eom', 'date', 'days', 'power kw/h', 'cons power', 'av day.2']]
df_power.to_csv('data_storage/power.csv', index=False)

df_gas = df[['date_eom', 'date', 'days', 'gaz m3', 'cons gaz', 'av day']]
df_gas.to_csv('data_storage/gas.csv', index=False)