age = 17
grade = 85
if age >=18 and grade >=85:   #Loop will end when if statement ends if it is true.
    print ("A-Excellent")     #here we used two if conditions, so it will execute and print two if statements if it is true.
if age>=18 and grade>+70:
    print("B-Good")
else: 
    print("c-fail in the exam")


in_temp=35
out_temp= 25
if in_temp>30 and out_temp>20:      #here only one if condition, so the loop will end after executing one if statement.
    print("it is good day")
elif in_temp<40 and out_temp<30:
    print("its a cool day")
else:
    print("normal day")

score= 75
if score>=90:
    print("A+--excellent")
elif score>80:
    print("b--good")
elif score>70:
    print("c--average")
else:
    print("fail")


"""Nested if else statement in python"""

has_ticket = False
age = 19
if has_ticket:
    if age>=18:
        print("enjoy your movie")
    else:
        print("need supervision by employer")
else:
    print("please buy a ticket first")
