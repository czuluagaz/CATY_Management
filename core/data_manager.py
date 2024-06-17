# data_manager.py
# path: /functions
# date 2024-06-08
# author C. Zuluaga
# version 1.0

"""
This module contains the functions to manage the data from the dataset.
"""

# Importing the necessary libraries
import pandas as pd


# Function to convert .csv file to pandas dataframe
def csv_to_dataframe(
    file_path: str,
    sep: str = ",",
    decimal: str = ".",
    encoding: str = "utf-8",
    header: int = 0,
    index_col: int = 0,
    low_memory: bool = False,
) -> pd.DataFrame:
    """
    This function reads a .csv file and converts it to a pandas dataframe.
    """
    try:
        # Reading the .csv file
        data = pd.read_csv(
            file_path,
            sep=sep,
            decimal=decimal,
            encoding=encoding,
            header=header,
            index_col=index_col,
            low_memory=low_memory,
        )
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found")
        print("Please verify the file name and try again")
        exit()


# function to read the data
def read_data_csv_df(directory: str, filename: str) -> pd.DataFrame:
    """
    This function reads a .csv file and converts it to a pandas dataframe.
    """
    path = Path.cwd().parents[0]
    try:
        df = pd.read_csv(path.joinpath(directory, filename))
        return df
    except FileNotFoundError:
        print(f"File {filename} not found")
        print("Please verify the file name and try again, and path")
        exit()
