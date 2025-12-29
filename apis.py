import requests

longitude= 2.35
latitude= 48.85

url= f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url)

data= response.json()
print(data)
data["current"]


import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)
data= response.json()
print(data)


import requests

url = "https://official-joke-api.appspot.com/random_joke"

response= requests.get(url)
data= response.json()
print(data)
data["setup"]


#APIs with Fucnitons

import requests

def todays_weather(latitude, longitude):
   
    response= requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data= response.json()
    return data ["current"]['temperature_2m']
paris_temp= todays_weather(48.85, 2.35)
Londons_temp=todays_weather(51.50, -0.12)
tokyos_temp= todays_weather(35.68, 139.69)

print(paris_temp)
print(Londons_temp)
print(tokyos_temp)


import requests

def country_population(country_name):
    response= requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
    data= response.json()
    return data[0]["population"]
indias_population= country_population("India")
Americas_population= country_population("United States")
chaina_population= country_population("China")

print(indias_population)
print(Americas_population)
print(chaina_population)

import requests
from datetime import datetime, timedelta

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)


