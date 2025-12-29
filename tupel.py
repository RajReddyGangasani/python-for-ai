""" Tuples are immutable which we cannot change it once it is created"""
# it is used to store the fixed values, that should not change
numbers= (22, 33, 53, 76)

print(numbers)

x,y,z,a= numbers
print(x)

num=list(numbers)
print(num)

num.insert(1, 55)
print(num)
numbers=tuple(num)
print(numbers)