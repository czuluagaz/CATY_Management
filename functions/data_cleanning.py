# Data cleanning using pandas

import pandas as pd
import numpy as np

# Variables
# call dataframe from csv file
dataset = "data_storage/raw_data.csv"

# see the first 5 entries
df = pd.read_csv(dataset, decimal=",", delimiter=';')  # read the csv file and change ',' to '.'
print(df.head(5))

# nulmber of columns and rows
print(df.shape)

# get the columns names
print(df.columns)

# get the index
print(df.index)


# Variables
dataset = "data_storage/raw_data.csv"
df = pd.read_json("data_storage/clean_data.json")  # read the json file


# convert the csv file to a json file and standardize the columns names and type
def csv_to_json(dataset):
    df = pd.read_csv(dataset, decimal=",")  # read the csv file and change ',' to '.'
    df.to_json("data_storage/raw_data.json")
    # rename the columns
    df.rename(
        columns={
            "date": "date_meas",
            "T av": "temp_av_month",
            "days": "days_cons",
            "gaz m3": "gas_meas_m3",
            "cons gaz": "gas_cons_m3",
            "av day": "gas_av_day_cons_m3",
            "Unnamed: 6": "gas_m3_to_kwh_1",
            "Unnamed: 7": "gas_m3_to_kwh_2",
            "water m3": "water_meas_m3",
            "cons": "water_cons_m3",
            "av day.1": "water_av_day_cons_m3",
            "power kw/h": "power_meas_kw/h",
            "cons power": "power_cons_kw/h",
            "av day.2": "power_av_cons_day_kw/h",
        },
        inplace=True,
    )
    # convert columns to numeric
    # df = df.isnull().sum() # check for null values
    # df = df.fillna(0) # fill null values with 0
    # df['date_meas'] = pd.to_datetime(df['date_meas'], dayfirst=True, errors='coerce') # convert the column to datetime
    # df['date_meas'] = df['date_meas'].dt.strftime('%d/%m/%Y') # convert the column to datetime
    # df['days_cons'] = df['days_cons'].astype('int')
    # df['days_cons'] = df['days_cons'].astype('int') # convert the column to numeric
    df["temp_av_month"] = pd.to_numeric(
        df["temp_av_month"], errors="coerce"
    )  # convert the column to numeric
    # chnage NaN to null
    df = df.replace(np.nan, "", regex=True)
    """
    df['gas_meas_m3'] = pd.to_numeric(df['gas_meas_m3'], errors='coerce') # convert the column to numericcsv
    df['gas_cons_m3'] = pd.to_numeric(df['gas_cons_m3'], errors='coerce') # convert the column to numeric
    df['gas_av_day_cons_m3'] = pd.to_numeric(df['gas_av_day_cons_m3'], errors='coerce') # convert the column to numeric
    df['gas_m3_to_kwh_1'] = pd.to_numeric(df['gas_m3_to_kwh_1'], errors='coerce') # convert the column to numeric
    df['gas_m3_to_kwh_2'] = pd.to_numeric(df['gas_m3_to_kwh_2'], errors='coerce') # convert the column to numeric
    df['water_meas_m3'] = pd.to_numeric(df['water_meas_m3'], errors='coerce') # convert the column to numeric
    df['water_cons_m3'] = pd.to_numeric(df['water_cons_m3'], errors='coerce') # convert the column to numeric
    df['water_av_day_cons_m3'] = pd.to_numeric(df['water_av_day_cons_m3'], errors='coerce') # convert the column to numeric
    df['power_meas_kw/h'] = pd.to_numeric(df['power_meas_kw/h'], errors='coerce') # convert the column to numeric
    df['power_cons_kw/h'] = pd.to_numeric(df['power_cons_kw/h'], errors='coerce') # convert the column to numeric
    df['power_av_cons_day_kw/h'] = pd.to_numeric(df['power_av_cons_day_kw/h'], errors='coerce') # convert the column to numeric
    """

    # write the new dataset to a json file
    df.to_json("data_storage/clean_data.json", orient="records")
    return df


# csv_to_json(dataset) # call the function

# print 10 first rows
# print(df.head(20))
# If i call from datasource download the dataset from Delzu ECO-Life
# df = pd.read_json('data_storage/clean_data.json')


# columns_header = df.columns.tolist() # Get the columns header


# describe the dataset before manipulation
describe_dataset_before = df.describe()
print(describe_dataset_before)
# print(df.iloc[[df['gas_cons_m3'].idxmax()]]['date_meas']) # get the row with the max value of gas_m3_to_kwh_1

# sorting columns DF
# df.sort_values('date_meas', inplace=True) # sort the dataset by date_meas

# filtering rows conditioanlly
# print(df[(df['temp_av_month']<15) & (df['gas_cons_m3']>0)]) # filter the dataset by temp_av_month < 15 and gas_cons_m3 > 0

# group by
# print(df.groupby(['temp_av_month']).value_counts().head()) # group the dataset by temp_av_month and calculate the mean
# print(df.groupby('days_cons')['power_cons_kw/h'].mean().head()) # group the dataset by power_cons_kw/h and calculate the mean
# groupby and count
# print(df.groupby('days_cons')['power_cons_kw/h'].count().head()) # group the dataset by temp_av_month and count the rows

print(df.values[0][0])

# iterate over the rows of the dataset
# for index, row in df.iterrows():
#    print(index, row['temp_av_month'])

# for index, row in df.iterrows():
# print(row)
# if index == 1:
# break

print(df[["temp_av_month", "gas_cons_m3"]])

print(df.loc[:, ["temp_av_month", "gas_cons_m3"]])

print(df[0:10])