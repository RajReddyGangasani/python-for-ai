
#calling the object with self.

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return print(f"hi iam {self.name} and i am {self.age}")
    
    def greet(self):
        return print(" welcome to python course")
    
    def welcome(self):
        message = self.greet
        return print(f"hi how are you, {self.greet} ")

    
p1= student("raj", 26)
p1.last_name= "gangasani"
p1.house= "amaravaram"
print(p1.last_name)
p1.name= "naveen"
print(p1.name) #should not use the "()" while printing the attributes
del p1.age
print(p1.age) #will cause an error
p1.greet()


class person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def __str__(self):
        return print(f"hi i am {self.name} and i am {self.age} years old")
    
p1=person("raj", 25)
print(p1)
