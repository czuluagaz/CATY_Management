# Preprocessing the 3 csv files
# Version: 1.0
# Date: 2024-01-22

# import libraries
import pandas as pd

# create a list of the 3 csv files
files = ["water.csv", "power.csv", "gas.csv"]

# load the 3 csv files in a list of dataframes
dfs = [pd.read_csv(f"data_storage/{file}") for file in files]

# rename columns 4, 5 as 'cons' and 'av_day' respectively
# for df in dfs:
#     df.rename(columns={df.columns[4]: "cons", df.columns[5]: "av_day"}, inplace=True)

# convert date_eom and date to datetime
for df in dfs:
    df["date_eom"] = pd.to_datetime(df["date_eom"])
    df["date"] = pd.to_datetime(df["date"])

# # replace ',' with '.' in 'cons', 'av_day'
# for df in dfs:
#     df["cons"] = df["cons"].str.replace(",", ".").astype(float)
#     df["av_day"] = df["av_day"].str.replace(",", ".").astype(float)

# if 'cons' is NaN, 'days" = ""
for df in dfs:
    df["days"] = df["days"].where(df["cons"].notna(), "")

# add a column 'days_month' with number of days for each month in 'date_eom'
for df in dfs:
    df["days_month"] = df["date_eom"].dt.daysinmonth

# if 'date' is empty, fill with the first day of the month
for df in dfs:
    df["date"] = df["date"].fillna(df["date_eom"].dt.to_period("M").dt.start_time)

# # if av_day is empty interpolate the value between the previous and next value
# for df in dfs:
#     df["av_day"] = df["av_day"].interpolate()

# if in the label column is a 

# id av_day is empty, fill with the first value found descending in the column
for df in dfs:
    df["av_day"] = df["av_day"].fillna(method="bfill")

# add a column 'days_cons: if date is = to first day of the month then 'days_cons' = 'days_month' else 'days_cons' = 'date'- 'days_month'
for df in dfs:
    df["days_cons"] = df["date"].dt.to_period("M").dt.start_time
    df["days_cons"] = df["days_cons"].dt.daysinmonth
    df["days_cons"] = df["days_cons"].where(
        df["date"] == df["date"].dt.to_period("M").dt.start_time, df["date"].dt.day
    )

    df["missing_days"] = df["days_month"] - df["days_cons"]

# add column 'calc_cons' with the result of 'av_day' * 'days_cons' + next month 'av_day' * 'missing_days'
for df in dfs:
    df["calc_cons"] = (
        df["av_day"] * df["days_cons"] + df["av_day"].shift(-1) * df["missing_days"]
    )
    df["calc_cons"] = df["calc_cons"].fillna(df["av_day"] * df["days_cons"])

# sum of 'calc_cons' and compare with 'cons'
for df in dfs:
    df["diff_cons"] = df["cons"] - df["calc_cons"]

# add a column duplicate if the row eom_date is duplicated and fill with True
for df in dfs:
    df["duplicate"] = df.duplicated(subset="date_eom", keep=False)

# add a column join 'duplicate' and 'cons' and fill with True if 'duplicate' is True and 'cons' is NaN
for df in dfs:
    df["cons_duplicate"] = df["duplicate"] & df["cons"].isna()

# drop rows with 'cons_duplicate' = True
for df in dfs:
    df.drop(df[df["cons_duplicate"]].index, inplace=True)

# drop columns 'duplicate' and 'cons_duplicate'
for df in dfs:
    df.drop(columns=["duplicate", "cons_duplicate"], inplace=True)
    
# for dfs[2]: add a column kwh with the result of cons * 11,6
dfs[2]["conv_m3_kwh_month"] = dfs[1]["calc_cons"] * 11.6

# remove rows 

print(dfs[2].head(50))
print(dfs[0].describe())


# # add column 'calc_cons' with the result of 'av_day' * 'days_cons' + previous month 'av_day' * 'missing_days' except for the first month
# for df in dfs:
#     df["calc_cons"] = df["av_day"] * df["days_cons"] + df["av_day"] * df["missing_days"].shift(1)
#     df["calc_cons"] = df["calc_cons"].fillna(df["av_day"] * df["days_cons"])

# # add column 'diff_cons' with the difference between 'cons' and 'calc_cons'
# for df in dfs:
#     df["diff_cons"] = df["cons"] - df["calc_cons"]

# dfs to csv
for i, df in enumerate(dfs):
    df.to_csv(f"data_storage/{files[i]}", index=False)
