import datetime as dt
import requests
import pandas as pd
from IPython.display import display
import csv

# http://dataservice.accuweather.com/forecasts/v1/daily/1day/{locationKey}
BASE_URL = "http://dataservice.accuweather.com/locations/v1/adminareas/"
API_KEY = "gJGoIPoyKLYIpCKGrCg5Nj9tb84NjjWQ"
CITY = "Marikina"

url = BASE_URL + API_KEY

response = requests.get(url).json()

print(response)