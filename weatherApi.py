import datetime as dt
import requests
import pandas as pd
from IPython.display import display
from dateutil import tz
import csv

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "405af6a3d70c1a804713877c3eceb864"
CITY = "Manila"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

# Convert to PH
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Asia/Kolkata')

weather = response['weather']
temperature = response['main']['temp']
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']



# print(temperature)