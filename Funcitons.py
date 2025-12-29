"""Functions are the block of code which is used to reuse the code many times without writing extra code"""
def greet():
    print("hello")
    print("hello users")
greet()

#lets calculate wether using python function and if statements.
def todays_weather():
    temprature =25
    if temprature <20:
        print("it is a clod day")
    else: 
        print("it is a hot day")
todays_weather()


#lets use some globla and local variables

clas = 10
def standard_name():
    print(f"standard of raj is {clas}")
standard_name()

temp = 30     #global variable
def todays_temp():
    temp = 25  #local variable which will be priotorized within the function
    if temp>20:
        print(f"temp is {temp}, its a hot day")
    else:
        print(f"temp is {temp}, its a cold day")
todays_temp()




#lets learn about parameters within the funciton which are used to pass the inputs to the function

def greet(name):
    print(f"hello {name}")
greet("raj")


def intro(name, age):
    print(f"hi i am {name}")
    print(f"and i am {age} old")
intro(name="raj", age=25)
intro(name="naveen", age=23)
intro(name="sandeep", age=21)


def total_price(price, tax_rate, discount):
    tax=price*tax_rate
    total_price= price+tax-discount
    print(f"total price is {total_price}")
total_price(price=50,tax_rate=0.08, discount=10)

               #OR#

def total_price(price=50, tax_rate=0.08, discount=10):
    tax=price*tax_rate
    total_price= price+tax-discount
    print(f"total price is {total_price}")
total_price()


# Return is used to return the end results which can be used in furhter.
# just print stateent will print the results but can not be stored and reuse it later.



def calculated_area(width, length):
    area= width*length
    return area
result=calculated_area(10,5) #here variable result is storing the first area value and you must pass the values here and this will be considered as first call
print(f"total area is {result}")   
result=calculated_area(5,5) #here variable result is storing the second area value, this will be considered as second call
print(f"total area is {result}")


