"""practice question of lecture 2 STRINGS AND CONDITIONAL STATEMENTS
"""

# question 1  WAP to input  user's first name and print its length

str="the $ $ $ $ is in my list"

print("the occurrence of $ in my string is:",str.count("$"))


#  question 2 WAP to  input user's first name  and print its length 

name=input("enter your first name ")

print("the length of your first name is: ", len(name))


#  Quedtion 3 WAP to check if a number is entered by the user is odd or even

number= int(input("enter the number the to check: "))


if number%2==0:
    print("number is even")

else:
    print("number is odd")


#  question 4 WAP to find the greatest of 3 numbers entered by the user 

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

if (a>=b and a>=c):
    print("A is greater")

elif(b>=c):
    print(" B is greater")

else:
    print("C is greater")


# question 5 WAP to check if a number is multiple of 7 or not


number= int(input(" enter a number: "))

if (number%2==0):
    print("multiple of seven")

else:
    print("Not a multiple of seven ")











    


