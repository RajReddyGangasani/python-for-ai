######################___________________________________#####################
import requests
from datetime import datetime, timedelta           #timedelta is a class which is used when you want time differece

today= datetime.now()
week_ago= today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")         #here you converting the date from json to readable format
end_date= today.strftime("%Y-%m-%d")

url= f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response= requests.get(url)                         #here you are searching for the url in internet and birnging the data
data= response.json()
print(data)


import pandas as pd                                 #importing pandas librabry to create a dataframe

daily_data = data['daily']                          #you storing the above output "data" in daily_data

df= pd.DataFrame({

'date': daily_data['time'],                         #you are introducing data, max_temp, min_temp variable in dictornay to create those columns in table
'max_temp' : daily_data['temperature_2m_max'],
'min_temp': daily_data['temperature_2m_min']

})

print(df)


import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

plt.plot(df['date'], df['max_temp'], marker='o', label='Max temp')
plt.plot(df['date'], df['min_temp'], marker='o', label= 'Min temp')


plt.xlabel('Date')
plt.ylabel('Temprature')
plt.title('PARIS Weather last 7 days')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('wetherofpairs.png')
plt.show()

import os                   #this is a module used to create, check, delete, search the files in  the local system

if not os.path.exists('data'):               # if there is no such file called 'data' we creating it'
    os.makedirs('data')          
df.to_csv('data/paris_weather.csv')          #here we are converting 'df' file into csvformat file.
print("Data saved to data/paris_weather.csv")


