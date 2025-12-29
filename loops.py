for i in range(5):
    print(i)


for i in range(1,7):
    print(i)

count=0
for i in range(1,6):
    if i%2==0:
        count=count+1
print(count)

numbers=[10,20,70,40,90,100]
largest=0
for num in numbers:
    if num>largest:
        largest=num
print(largest)

text="hello world"
vowels="aeiou"
count=0
for char in text:
    if char.lower() in vowels:
        count=count+1
print(count)
