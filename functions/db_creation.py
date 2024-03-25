# Utilities management tool
# Function: DB creation and data insertion
# This script is to create SQL DBs, tables, and insert data
# Author: Camilo Zuluaga
# Date: 2024-03-23
# Version: 1.0
# Usage: python3 db_create.py

import sqlite3
import os
import sys
import pandas as pd
from sqlalchemy import create_engine

# Create a database
def create_db(db_name):
    conn = sqlite3.connect(db_name)
    conn.close()
    print(f"Database {db_name} created successfully")

# Create a table
def create_table(db_name, table_name, columns):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(f"CREATE TABLE {table_name} ({columns})")
    conn.commit()
    conn.close()
    print(f"Table {table_name} created successfully")

# Insert data into a table
def insert_data(db_name, table_name, data):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.executemany(f"INSERT INTO {table_name} VALUES ({data})", data)
    conn.commit()
    conn.close()
    print(f"Data inserted successfully")

# Create a table from a CSV file
def create_table_from_csv(db_name, table_name, csv_file):
    df = pd.read_csv(csv_file)
    engine = create_engine(f"sqlite:///{db_name}")
    df.to_sql(table_name, engine, index=False)
    print(f"Table {table_name} created successfully from {csv_file}")

# Main function
def main():
    db_name = "my_db.sqlite"
    table_name = "my_table"
    columns = "name TEXT, age INTEGER"
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    csv_file = "data.csv"

    create_db(db_name)
    create_table(db_name, table_name, columns)
    insert_data(db_name, table_name, data)
    create_table_from_csv(db_name, table_name, csv_file)

if __name__ == "__main__":
    main()

# End of script
    
create_db("utilities_track.db")