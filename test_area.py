import pandas as pd

df = pd.read_json('data_storage/clean_data.json') # read the json file
print(df.head(5))
df.info()
print(df.index)
df.columns
