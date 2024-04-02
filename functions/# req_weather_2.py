# Requst weather data from weatherandclimate.com
# Dater: 2023-12-01
# Version: 1
# Author: CZU

''' Develope a scraper  that gets the weather data from weatherandclimate.com'''

# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# initialize the timer
start = time.time()

# url
url = 'https://weatherandclimate.com/belgium/liege/beyne-heusay'

# get the response
response = requests.get(url)

# parse the response
soup = BeautifulSoup(response.text, 'html.parser')

# get the weather data
weather_data = soup.find_all('div', class_='col-md-6')

# print the weather data
print(weather_data)
print(len(weather_data))

# # get the date
# date = weather_data[0].find('h2').text

# # get the temperature
# temperature = weather_data[0].find('span').text

# # get the weather condition
# weather_condition = weather_data[0].find_all('span')[1].text

# # get the wind speed
# wind_speed = weather_data[0].find_all('span')[2].text

# # get the humidity
# humidity = weather_data[0].find_all('span')[3].text

# # get the pressure
# pressure = weather_data[0].find_all('span')[4].text

# # create a dictionary
# weather_dict = {
#     'date': date,
#     'temperature': temperature,
#     'weather_condition': weather_condition,
#     'wind_speed': wind_speed,
#     'humidity': humidity,
#     'pressure': pressure
# }

# # create a dataframe
# weather_df = pd.DataFrame([weather_dict])

# # check if the file exists
# if os.path.exists('data_storage/weather_data.csv'):
#     # read the existing data
#     existing_data = pd.read_csv('data_storage/weather_data.csv')
#     # append the new data
#     new_data = pd.concat([existing_data, weather_df], ignore_index=True)
#     # save the data
#     new_data.to_csv('data_storage/weather_data.csv', index=False)
# else:
#     # save the data
#     weather_df.to_csv('data_storage/weather_data.csv', index=False)

# # calculate the time taken
# end = time.time()
# time_taken = end - start

# # print the time taken

# print(f'Time taken: {time_taken} seconds')

