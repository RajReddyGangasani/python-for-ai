a=25            # integer datatype
b=20.55         # float datatype
c="hello raj"   # string datatype
d=True          # boolean datatype

print(a,c)

print(str(a) + " " +c) #you can not concatenate integer with string directly, you need to cclaonvert integer into string using str() function.

print("my name is" + c + "and iam f{a} year old") #this is another method to concatenate string with f-string= f{variable_name}

if a>=26:
    print("he is eligible for dancing")
else:
    print("he is not eligible for dancing") #this if else condition uses boolen datatype.

