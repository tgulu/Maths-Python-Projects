c = False
a = 0
b = 0
x = False 
while c !=True:
    while not x:
        print("Division program")
        a = int(input("Enter a number to divide: ")) 
        b = int(input("And a number to divide by: ")) 
        if b != 0:
            result = a/b
            break
        elif  a != 0:
            result = a/b
            break
    if a == 0 or b == 0:
        print("enter again")
    else:
        print("Answer:", result)
        
    c = True