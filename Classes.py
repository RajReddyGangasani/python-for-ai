# STEP 1: DEFINING A CLASS
# ------------------------
# A class is a blueprint.
# It describes what an object should have (data)(variables = name, age, course) STEP: 2
# and what it can do (actions) (introduce, study, Age) STEP: 2

class Student:


    # STEP 2: CONSTRUCTOR (__init__ METHOD)
    # ------------------------------------
    # This function runs automatically
    # when a new object is created from the class.
    # It is used to assign values to the object

    def __init__(self, name, age):
        self.name= name
        self.age= age


    

     # STEP 3: METHOD (ACTION)
    # -----------------------
    # This is a function inside a class.
    # It defines what the object can do.

    def introduce(self):
        print(f"Hi my name is {self.name}")
        print(f"And i am {self.age} old")
    
    def study(self):
        print(f"I am {self.name} and i am studying python")

    def Age(self):
        print(f"i am {self.age} old")




# STEP 4: CREATING OBJECTS
# -----------------------
# Now we create real objects using the Student class.
# Each object is independent.
    
student1 = Student("Raj", 26)       #object1
student2= Student("Naveen", 24)     #object2 




# STEP 5: USING OBJECT DATA AND METHODS (Actions)
# -------------------------------------
# Call methods using object name

student1.introduce()
student1.study()
student1.Age()
student1.age




# STEP 6: INHERITANCE
# ------------------
# A new class can reuse another class.
# This avoids rewriting code.

class CollegeStudent(Student):

    def __init__(self, name, age, course):      #Constructour (properties)
        super().__init__(name,age)
        self.course= course

    def course_details(self):                   #Actions
        print(f"i am sutding {self.course}")
    
    def name_course(self):                      #Actions
        print(f"i am {self.name} and i am studying {self.course}")
    
student3= CollegeStudent("Raj", 15, "Gen AI")   #Creating Objects
student3= CollegeStudent("Naveen", 13, "Machine Learing & Data Engineering")

student3.course_details()                       #Calling Methods using objects
student3.name_course()