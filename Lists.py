age = 25
had_licence = False
had_vahicle = False
my_list= ["raj",24,"Good", had_licence, had_vahicle]

print(my_list[2:3])

#to add items to the list
fruits = ["apple","banana", "orange"]
fruits[0]= "mango"        #add and override the list
print(fruits)

fruits.append("guava")     #add item in the end
print(fruits)

fruits.insert(3,"grapes")  #add item in the spot
print(fruits)

#to delete the items from the list
fruits.remove("grapes")     #remove item form the list
print(fruits)

fruits.pop()                # del the last item
print(fruits)

del fruits[2]            # removes the item by index
print(fruits)


numbers=[1,3,2,6,4,10]
print(numbers.count(1))
print(numbers.index(2))
numbers.sort()      #sort the list in order
print(numbers)
