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



