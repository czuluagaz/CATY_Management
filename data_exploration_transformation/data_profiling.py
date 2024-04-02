# import ydata_profiling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ydata_profiling


# Load the data from csv file meterdata_table_sanitized.csv
# data = pd.read_csv('meterdata_table_sanitized.csv')

# function to create a profile report from a chosen dataset
def create_profile_report(data):
    # create a profile report
    profile = ydata_profiling.ProfileReport(data)
    profile.to_file('data_exploration_transformation/clean_data.html')

    return profile

# Load the data from data_storage\gas.csv
data = pd.read_csv('data_storage/gas.csv')

# Display the first 5 rows of the data
print(data.head())

# create a profile report
profile = ydata_profiling.ProfileReport(data)
# profile = ProfileReport(data, title="Profiling Report", explorative=True)
profile.to_file('data_exploration_transformation/clean_data.html')
