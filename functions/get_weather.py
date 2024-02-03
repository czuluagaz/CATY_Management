# Get weather from OpenWeatherMap
# other https://weatherandclimate.com/belgium/liege/beyne-heusay

# links: https://openweathermap.org/api/one-call-api
# https://openweathermap.org/current
# https://openweathermap.org/weather-data
# https://openweathermap.org/api/one-call-api
# https://openweathermap.org/weather-conditions

# in order to get the weather data from OpenWeatherMap you need to create an account and get an API key
# https://home.openweathermap.org/api_keys
# https://openweathermap.org/api/one-call-api

# import libraries
import requests
import json


# API key
api_key = '266895e794130d12da86325780cc0e0b'

# base url
base_url = 'http://api.openweathermap.org/data/2.5/onecall?'

# get the latitude and longitude from the dataset
lat = 50.62251 
lon = 5.66508

# complete url
complete_url = base_url + 'lat=' + str(lat) + '&lon=' + str(lon) + '&exclude=hourly,minutely&units=metric&appid=' + api_key

# get the response
response = requests.get(complete_url)

# convert the response to json format
weather_data = response.json()

# print the response
print(weather_data)

# write the response to a json file
with open('data_storage/weather_data.json', 'w') as json_file:
    json.dump(weather_data, json_file)

# read the json file
with open('data_storage/weather_data.json') as json_file:
    weather_data = json.load(json_file)

# print the response
print(weather_data)

# get the current weather
#current_weather = weather_data['current']

# get the current temperature
#current_temp = current_weather['temp']

# get the current humidity
#current_humidity = current_weather['humidity']





