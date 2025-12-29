class Dog:
    def __init__(self, name, barking):
     self.name= name
     self.barking= barking

    def bark(self):
     print(f"hi this is {self.name} and it barks as {self.barking}")

dog1= Dog(name= "germanShepard", barking= "howw")
dog2= Dog(name= "husky", barking= "bowbow")

dog1.bark()
dog2.bark()

class Age(Dog):
  
  def __init__(self, name, barking, age):
    super().__init__(name, barking)
    self.age= age

  def intro(self):
    print(f"hi this is {self.name} and it barks as {self.barking} and its age is {self.age}")  

Dog1= Age("germanshepard", "how", 5 )
Dog2= Age("huskey", "bow", 4)

Dog2.intro()
Dog2.intro()