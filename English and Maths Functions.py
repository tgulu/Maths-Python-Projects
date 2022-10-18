"""
Maths and English Functions
ex0 - Square Root
ex1 - Pythagoras
ex2 - Fibnumber
ex3 - Table Creator 
ex4 - Length of Word
ex5 - How Many Vowels
ex6 - Encryption Key 
ex7 - Triangles
"""

from math import sqrt

def ex0():
    i = int(input("Enter a non-negative integer: "))
    if i<0:
        print("Negative numbers do not have real square roots")
    else:
        root = sqrt(i)
        print("The square root is", round(root, 2))
        
def ex1() :
    from math import sqrt
    from math import acos
    from math import degrees
    #importing the needed maths moduels 
    pythagoras = True


    while pythagoras == True:
        try:
            hypotenuse = float(input("Please Enter the Hypotenuse: "))
            width = float(input("Please Enter the Width: "))    
            #Checks if the user has entered the right information         
            while hypotenuse <= 0 or width <= 0 or hypotenuse <= width:  
                print("Please Enter a Hypotenuse > Width and > 0 :")
                hypotenuse = float(input("Please Enter the Hypotenuse:"))
                width = float(input("Please Enter the Width: "))

            height = sqrt(hypotenuse**2 - width**2)
            print ("The Length Of The Height Is","{:.2f}".format(height))
            # Will alert the user they're added in the wrong information 
            pythagoras = False
        except:
            print("You Have Not Entered An Integer, Please Enter a Hypotenuse and Width Again")
            continue

    angle_1 = acos(width/hypotenuse)
    conversion = degrees(angle_1)
    print ("Interior Angle 1 is :","{:.2f}".format(conversion),"\u00b0")

    angel2 = 180-90-conversion
    print ("Interior Angle 2 is", round(angel2,2),"\u00b0")




    
    
def ex2() :
    valid = False
    while valid == False:
           valid = True
           numberofterms = int(input("How Many Terms Do You Want: "))
           # Checks if the value entered is greater than 0; if not the sequence can't work
           if numberofterms < 0: 
               print("Value for number of terms must be positive!")  
               valid = False
        

    fibnumber = 0
    termnumber = 1
    for i in range(numberofterms):
        print(fibnumber, end= " ")
        termnumber = fibnumber+termnumber
        fibnumber = termnumber - fibnumber

    
    
def ex3() :


    table = True
    counter = 1
    while table == True:
          try:
                colums = int(input("Enter How Many Colums Do You Want: "))
                rows = int(input("Enter How Many Rows Do You Want: "))
                if colums<=0 or rows<=0:
                      raise ValueError
                for i in range(1, rows +1):
                    
                    for a in range(1,colums+1):
                        maxlength = len(str(rows**colums)) + 1
                        print(" " * (maxlength - len(str(i**a))),end="")
                        print(i**a,end="")
                    print("")
                    
                              


                table= False
          except(ValueError):
                     print("You Have Not Entered A Positive Integer, Please Enter Again")
                     continue 

    
def ex4() :
 
    def longest_word(word_list):
        longest_word = " "
        for word in word_list:
            if len(word) > len(longest_word):
                longest_word = word
        print ("The Length of The Longest Word is",len(longest_word))
    # defining and finding the length of the longest word
    def shortest_word(word_list):
        shortest_word = " "*1000
        for word in word_list:
            if len(word) < len(shortest_word):
                    shortest_word = word
        print ("The Length of The Shortest Word is ",len(shortest_word))
    words = input("Please Enter a Line of Text: ")
    word_list = words.split()
    for word in word_list:
        print(word)
    longest_word(word_list)
    shortest_word(word_list)
    
    
def ex5() :
    words = input("Enter a Line of text: ")



    words = words.lower()
    vowel_a = words.count("a")
    vowel_e = words.count("e")
    vowel_i = words.count("i")
    vowel_o = words.count("o")
    vowel_u = words.count("u")



    if vowel_e + vowel_a + vowel_u + vowel_o + vowel_i == 0:
        print("No vowels found")
    else:
        biggest_vowel=0
        for text in [vowel_e , vowel_a ,vowel_u, vowel_o, vowel_i]:
            if text > biggest_vowel:
                biggest_vowel = text
 
        if biggest_vowel == vowel_a:
            print ("The Most Frequently-Occurring Vowel Is A")
            print ("And The Number of Occurrence Is", biggest_vowel)
        if biggest_vowel == vowel_e:
            print ("The Most Frequently-Occurring Vowel Is E")
            print ("And The Number of Occurrence Is", biggest_vowel)
        if biggest_vowel == vowel_i:
            print ("The Most Frequently-Occurring Vowel Is I")
            print ("And The Number of Occurrence Is", biggest_vowel)
        if biggest_vowel == vowel_o:
            print ("The Most Frequently-Occurring Vowel Is O")
            print ("And The Number of Occurrence Is", biggest_vowel)
        if biggest_vowel == vowel_u:
            print ("The Most Frequently-Occurring Vowel Is U")
            print ("And The Number of Occurrence Is", biggest_vowel)
        


    
def ex6() :
    running = True
    while running==True:
        ready =False
        while(ready==False or  words.isupper()==False or words.isspace == False):
            try:
                key = int(input("Enter the encryption key, or enter 0 to quit: "))
                if key == 0:
                    break
                words = str(input("Please Enter a Upper Case Line of Text: "))
                if(words.isupper()):  ready=True
              

                else:
                    print("Please Type an Upper Casesed Word")
            except:
                print("Make sure key is an integer")
        if key == 0:
            break
        final_string = ""
                
        for i in  words:
            if i !=" ":
                ascii_char =ord(i)
                sub_char = (ascii_char - 65)
                key_char = ( sub_char + key)
                mod = key_char%26
            
                encrypt = mod + 65
                final_string = final_string + chr(encrypt)
            else: final_string = final_string + " "

        print(final_string)
  
                

    
def ex7() :
    valid = False
    while valid == False:
        valid = True

        rows = int(input("Please Enter The Length of The Innermost Triangle: "))
        
        if rows % 2 != 1 or rows <= 1:
            print("Please Enter an Odd positive intger ")
            valid = False
        chr1 = input("Please enter 1 charcter: ")
        chr2 = input("Please enter 2 charcter: ")
        chr1 = chr1[0]
        chr2 = chr2[0]


    acc = rows
    spaces = 0
    #TRIANGLE 1
    for x in range(0,(rows+1)//2):
        print(" " * spaces + chr1 * acc )
        acc = acc - 2
        spaces = spaces + 1


    acc = 1
    spaces = rows
    acc2 = 0
    acc3 = 0
    #TRIANGLE 2 
    for y in range(0,rows+1):
        print(" " * spaces + chr2 * acc + chr1 * acc2 + chr2 * acc3)
        acc = acc + 2
        spaces = spaces - 1
        if y == ((rows-1)//2):
            acc = 1
            acc2 = rows
            acc3 = 1
        if y > ((rows-1)//2):
            acc2 = acc2 - 2
            acc3 = acc3 + 2


    acc = rows*2+1
    spaces = 0
    acc2 = 1
    acc3 = 0
    acc4 = 0

    #TRIANGLE 3 
    for z in range (0,((rows+3)//2) - 1):
        print(" "* spaces + (chr1* acc) + (chr2 * acc2) +( chr1* acc))
        acc = acc - 2
        acc2 = acc2 + 2
        
        spaces = spaces + 1
    acc = rows
    acc2 = 1
    for z in range (0,((rows+3)//2) - 1):
        print(" "* spaces + (chr1* acc) + (chr2 * acc2) +(chr1 * acc) + (chr2* acc2) + (chr1 * acc))
        acc = acc - 2
        acc2 = acc2 + 2
        spaces = spaces + 1


    acc = rows*2+1
    for z in range (0, acc):
        print(" " * spaces + chr1 * acc )
        acc = acc - 2
        spaces = spaces + 1
   
   


print("Welcome to Math and English Functions")
print("ex0 - Square Root\nex1 - Pythagoras\nex2 - Fibnumber\nex3 - Table Creator\nex4 - Length of Word")
print("ex5 - How Many Vowels \nex6 - Encryption Key \nex7 - Triangle")

# do not modify anything beneath this line
exlist = [None, ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex0]
running = True
while running :
    line = input("Select exercise (0 to quit): ")
    if line == "0" : running = False
    elif len(line)==1 and "1"<=line<="8": exlist[int(line)]()
    else : print("Invalid input - try again")


