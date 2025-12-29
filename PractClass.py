class Student:

    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def introduce(self):
        print(f" I am {self.name} and i am {self.age} old")

student1= Student("Raj", 25)
student2= Student("Nava", 24)

student1.introduce()
student2.introduce()

class StudentCourse(Student):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course= course

    def course_details(self):
        print(f"I am {self.name} and iam studing {self.course}")
    
student1= StudentCourse("Raj", 25, "Python with ai")
student2= StudentCourse("Nav", 23, "Python with ML")

student1.course_details()
student2.course_details()


class Dog:
    def __init__(self, name, breed):
        self.name= name
        self.breed= breed
    
  
jerry=Dog(name= "jerryFred", breed="labardor")
furry= Dog(name="furreyfine", breed="huskey")

jerry.breed
furry.name


class BankAccount:

    def __init__(self, owner_name, balance):
        self.owner_name= owner_name
        self.balance= balance

    def show_balance(self):
        print(f"i am {self.owner_name} and my totalbalance is {self.balance}")

    def deposite(self,amount):
        self.balance= self.balance+amount
        print(f"your deposite amount is {amount}")
        self.show_balance()
    
    def withdraw(self, amount):
    
        if amount > self.balance:
            print("Insufficent Balance")
        else: 
            self.balance= self.balance- amount
            print(f"your with drasl amount is {amount}")



user1= BankAccount(owner_name= "Raj", balance= 1000.00)
user2= BankAccount(owner_name= "Yogi", balance=100.00)


user1.show_balance()
user1.deposite(200)
user1.withdraw(100)
user2.show_balance()
user2.deposite(300)
user2.withdraw(150)


    