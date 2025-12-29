#convert the negative number to positive.
n=-5
if n<0:
    print(n*-1)
else:
    print(n)


a=13
if a%2==0:
    print("a is a even number")
else:
    print("a is a ood number")


b=50
c=40
if b>c:
    print(b)
else:
    print(c)

password=input("enter your password")
if len(password)>=6:
    print("storng password")
else:
    print("weak password")

x=10
y=10
z=40
if x==y and y==z:
    print("equalaterail triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("invilid numbers")

t=0
if t>=30:
    print("its a hot day")
elif t>=20:
    print("its a warm day")
elif t>=10:
    print("its a cool day")
else:
    print("its terrible cold day")