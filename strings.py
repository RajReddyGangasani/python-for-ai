"""Different ways to concatenate strings in python
"""
name="raj"
wish ="good morning"
print(wish+" "+name) #concatenate using + operator

name="raj"
age=25
print(f"my name is {name} and i am {age} year old")  #f-string is used to concatenate srtings with other or number.



""" Below following methods are of manupulating the strings in python"""

message="  hello raj , welcome to python programming  "
price= "$200"

print(message.upper())
print(message.lower())
print(price.strip("$"))
print(message.title())

print("python" in message)
print(message.startswith("raj"))
print(message.endswith("programming"))
print(message.replace("python", "java"))

print(message.find("raj"))
print(message.count("r"))




