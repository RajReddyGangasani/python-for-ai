import pandas as pd
import matplotlib.pyplot as plt

dates = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
max_temp = [30, 32, 31, 29, 28, 27, 26]
min_temp = [20, 21, 19, 18, 17, 16, 15]

df= pd.DataFrame({
    'Dates': dates,
    'Max_Temp': max_temp,
    'Min_Temp': min_temp
})
print(df)


import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))

plt.plot(df['Dates'], df['Max_Temp'], marker='o', label='Max temparature')
plt.plot(df['Dates'], df['Min_Temp'], marker='o', label= "Min temparature")

plt.xlabel['Date']
plt.ylabel['Tempratue']
plt.title("Weekly weather report")
plt.label()

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


