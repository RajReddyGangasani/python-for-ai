a=10
b=20
def addtion():
    total=a+b
    return total
addtion() #this will print and return 30

def highest_num():
    a=100
    b=40
    c=30
    if a>b and a>c:
        print("a is the big number")
    elif b>a and b>c:
        print(" b is bigger number")
    else:
        print("c is big number")
highest_num()
        

def even_or_odd(num):
    if num%2==0:
        return "EVEN"
    else:
        return "ODD"
print(even_or_odd(10))
print(even_or_odd(25))

def ovel_count(ov):
    ovels="aeiou"
    count=0
    for char in ov:
        if char in ovels:
            count=count+1
    return count
ovel_count("hello world")


def reverse_string(string):
    reverse_order=''
    for char in string:
        reverse_order=char+reverse_order
    return reverse_order
result = reverse_string("hello")
print(result)


def remove_dup(lists):
    orginal= set(lists)
    return orginal
remove_dup([10,20,30,20,20])


def largest_num(lists):
    highest=0
    for num in lists:
        if num>highest:
            highest=num
    return highest
print(largest_num([10,200,30,40,100]))

