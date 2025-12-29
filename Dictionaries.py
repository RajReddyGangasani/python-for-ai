person={
    "name": "raj",
    "age": 25,
    "class": "second"
}

# retreiving info form dictionaries
print(person["name"])
print(person["age"])

print(person.get("name"))

# adding the items to dectionaries
person["name"] = "naveen"
person["city"]= "Hyderabad"

print(person)

# deleteing items from the dectionaries 

del person["name"]
age= person.pop("age")

print(person)

print(person.keys())
print(person.values())

#to update multiple values
person.update({"name": "sandeep", "age": 24, "city": "hyderabad"})
print(person)


#dectionary inside the dectionary

students = {
    "raj": {"age": 25, "city": "newyork"},
    "naveen": {"age": 24, "city":"amaravaram"},
    "sandeep": {"age": 22, "city": "amaravaram"}
}
print(students)

print(students["raj"])
print(students.get("naveen"))
students['raj']["email"]= "raj@gmail.com"
print(students)
