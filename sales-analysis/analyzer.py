import os
import pandas as pd
import json


current_directory= os.getcwd()
print(current_directory)

data_path= "data/data.csv"
if os.path.exists(data_path):
    print("Yes File Found")
else:
    print("File Not Found")
    print("make sure you are running from the sales-analysis folder")

#here we are just readig the file and creating a data frame and storing the data in that dataframe
df = pd.read_csv('data/data.csv')
print("CSV Data")
print(df)

#hear we are creating another column "total" by calculating the quanitty and price
df['total']= df['quantity']* df['price']
print(df)

#to print the quantity rows that are having more than 2
print(df[df['quantity']==2])
#to print the the rows that with the data after the below data.
print(df[df['date']>"2024-01-03"])

#here we converting all totoal column values in to strings.
df['total']= df['total'].apply(str)
print(df['total'])

os.makedirs('out_out', exist_ok=True)

#converting the file formats
df.to_json('out_out//data.json', orient='records', indent=2)
print(df)

df.to_excel('out_out/data.xlsx', index=False)
print(df)

df.to_csv('out_out/sales_with_total.csv', index=False)

print("Files saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")

