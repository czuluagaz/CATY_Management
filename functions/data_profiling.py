# import ydata_profiling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ydata_profiling

# Load the data from data_storage\gas.csv
data = pd.read_csv('data_storage/gas.csv')

# Display the first 5 rows of the data
print(data.head())

# create a profile report
profile = ydata_profiling.ProfileReport(data)
# profile = ProfileReport(data, title="Profiling Report", explorative=True)
profile.to_file('data_storage/clean_data.html')
