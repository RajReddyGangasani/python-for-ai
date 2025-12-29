#with this code we are identifing the charlotte weather and creating a roport for past seven days
import requests                  #importing requesting library which helps to interact with all APIs

longitude= -80.851715            #we define the city name and location with help of latitude and longitude.
latitude = 35.362071
#below one is the url for calling the weather website API
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response= requests.get(url)       #we are getting the url and storing in response
data= response.json()             #converting the response data into json format.
print(data)

import requests
import datetime                   #we importing the datetime library which is used to define and calculate the dates.
from datetime import datetime, timedelta       #form datetime library we are importing datetime, timedelta(which is used to go for prevous dates)
import pandas as pd               #pandas is used to deal with tabular data
import matplotlib.pyplot as plt   #matplotlit is used to visualization (basic, plots, charts)
import os                         #os is used to control the operating system(local), save, retrive, delete, update files in local system.

longitude= -80.851715
latitude = 35.362071

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date= week_ago.strftime("%Y-%m-%d")
end_date= today.strftime("%Y-%m-%d")

url=  f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response= requests.get(url)
data= response.json()
print(data)

daily_data= data['daily']             #form data we are slicing the "daily" atribute and storing it in daily_data

df= pd.DataFrame({                    #creating a table form of the data stored in dailyslice.
    'Date': daily_data['time'],
    'Max_Temp': daily_data['temperature_2m_max'],
    'Min_Temp': daily_data['temperature_2m_min']

})

print(df)

plt.figure(figsize=(10,8))          #defining the figure size

plt.plot(df['Date'], df['Max_Temp'], marker= 'o', label='Maximum Temprature') #defineing the "x axis" with date and 'Y' axis with max_temp (drawing plot), and creating a dots at datesand labels
plt.plot(df['Date'], df['Min_Temp'],marker= 'o', label='Minimum Temprature')

plt.xlabel('Date')              #naming the x axis
plt.ylabel("Temprature c")      #naming the y axis
plt.legend()                    #corner labels
plt.title("CHARLOTTE Weather")  #giving title to the chart


plt.tight_layout()              #used to give perfect layouts without breaks.
plt.xticks(rotation=45)         # turning the x axis dates to 45 digrees

plt.savefig("Charlotte_weather.png")        #saving the file to local system

plt.show()                    #viweing the file


#conveting the dataframe file to csv file and storing it in local

if not os.path.exists('charlotte_data'):      #creating the new direcotry "charlotte_data" if not already existed
    os.makedirs("charlotte_data")

#converting the "df dataframe" to csv and storing in direcotry "charlotte_data" with the name of charlotte_weather_file.
df.to_csv('charlotte_data/charlotte_weather_file', index=False)   #specifing index=false cuz you are telling dataframe to store without index values.  
print("data is saved in file")




