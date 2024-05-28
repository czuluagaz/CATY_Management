# Create a SQLite database  from CSV files
# Usage: python3 create_db.py
# Author: CZU
# Date: 2023-12-01


# Importing required libraries
import sqlite3
import csv
import time

# Initialize the timer
start = time.time()

# Create a new SQLite database
conn = sqlite3.connect('utilities.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create a table for the electricity data
cursor.execute('''CREATE TABLE electricity_tb
                (id INTEGER PRIMARY KEY,
                date TEXT,
                time TEXT,
                consumption REAL,
                cost REAL)''')
