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

# change name of 6 and 7 columns
df.rename(columns={'Unnamed: 6': 'consumption', 'Unnamed: 7': 'cost'}, inplace=True)



print(df.head(5))


