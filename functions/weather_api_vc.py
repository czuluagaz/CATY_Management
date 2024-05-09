weather_api_vc.py

# Import weatehr temrperature from CV and add the ifno to csv file
# Import the necessary libraries
import requests
import csv
import os
from datetime import datetime

# Define the API key and the base URL
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY = "Vancouver"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

# Send a GET request to the server to get the weather details
response = requests.get(URL)

# Convert the response to JSON format
data = response.json()

# Get the main data block from the JSON data
main = data['main']

# Get the temperature from the main data block
temperature = main['temp']

# Get the current date and time
date_time = datetime.now()

# Open the CSV file in append mode
with open('weather_data.csv', mode='a') as file:
    writer = csv.writer(file)
    # Write the data to the CSV file
    writer.writerow([date_time, temperature])
    print("Data written to the CSV file")

# End of the program
print("End of the program")
