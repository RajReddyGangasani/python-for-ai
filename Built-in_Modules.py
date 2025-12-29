import math

root= math.sqrt(16)
print(root)
   #or#
from math import sqrt
root2= sqrt(36)
print(root2)


import random
numbers= random.randint(1, 10)
fruit= random.choice(["raj", "naveen", "sandeep", "varshini"])

print(numbers)
print(fruit)


import pandas as pd

data = {"Name": ["raj", "naveen"], "AGE": [25, 23]}

table1= pd.DataFrame(data)
print(table1)



import pandas as pd

data2 = {"NAME": ["Sandeep", "Naveen"], "COMPANYcode": [0.1, 0.2], "Company Name": ["Epam", "Cognizant"]}

table2= pd.DataFrame(data2)
print(table2)
