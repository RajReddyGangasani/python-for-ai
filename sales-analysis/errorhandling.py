#here we are learning error handiling

#Try and except is methond of error handiling

try:                           #In try we put riskey operation
    print(10/0)                # this is a riskey operation
except:                        #Except is nothing but , if the try(riskey operation fails, go ahed with the except but not throw the error)
    print("this could not be performed")



try:
    with open('data/date.csv', 'r') as f:
        content= f.read()
        print(content)
except: 
    print("this file does not exist")

