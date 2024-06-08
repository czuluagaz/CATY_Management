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
