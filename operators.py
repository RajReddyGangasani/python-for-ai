#Types of operators in Python
""" Arithmetic Operators """
print(10+5)  # = 15 is addition operator
print(10-5)  # = 5 is subtraction operator
print(10*6)  # = 60 is a multiplication operator
print(10/2)  # = 5.0  is a division operator
print(10%3)  # = 1 this is a modules operator will always gives reminder as answer
print(10//4) # = 2 this is a floor devision operatio, gives quotient as answer.

""" comparasion Operators """

age = 18

print(age == 18)    # True  - Equal to
print(age != 21)    # True  - Not equal to
print(age > 17)     # True  - Greater than
print(age < 20)     # True  - Less than
print(age >= 18)    # True  - Greater than or equal
print(age <= 18)    # True  - Less than or equal

""" Logical Operators """
age = 21
has_license = True
drunk = True
can_drive = (age >=18) and has_license and not drunk
print(can_drive)    # True - both conditions are true

height = 165
age = 25
is_eligible_for_ride = (height >= 150) or (age >=20)
print(is_eligible_for_ride)  # True - at least one condition is true

have_phone = True
can_sport = not have_phone
print(can_sport)   # False - negates the boolean value



""" Assignment Operators """
x = 10
x += 5      # x = x + 5
print(x)    # 15
x -= 3      # x = x - 3
print(x)    # 12
x *= 2      # x = x * 2
print(x)    # 24
