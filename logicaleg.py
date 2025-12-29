a=25
b="permitted"
can_allowed = (a>=18) and (b=="permitted")
print(can_allowed)

dance = "yes"
fight = "no"
can_perform = (dance=="yes") or (fight=="yes")  #alwasys use only comparision operator at this point.
print(can_perform)

flag = True
can_be_appointed = not flag
print(can_be_appointed)


n= 30
n_is_good = (n%2==0) and (n>22) and (n<51)
print(n_is_good)

correct_password = "admin123"
two_fac_auth = True
can_login = (correct_password=="admin123") and two_fac_auth==True
print(can_login)


a=15
b="intestellar"
can_watch = not (b=="intestellar") or (a==15)
print(can_watch)


age = 20
has_id = True
id_banned = False
allowed_entry = (age>=18) and (has_id==True) and (id_banned==False)
print(allowed_entry)

n="rajashekargangasani"
count=0
for char in n:
    if char=="a":
        count= count+1
print(count)


n=[12,45,23,67,34,89,90]
sum=0
for num in n:
    sum=sum+num
print(sum)


n=[12,45,100,67,34,89,90]
big=0
for num in n:
    if num>big:
        big=num
print(big)

st="hello"
rev=""
for char in st:
    rev= char + rev
print(rev)

items=["apple","banana","cherry"]
for item in (len(items)):
    print(item, items[i])
    