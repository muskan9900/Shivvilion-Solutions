""" pattern through loops """

#  q1 
""" printing a pattern 
*
* *
* * *
* * * *
* * * * *
"""

num=int(input("enter the number of rows : "))

#  for loop for the row
for i in range(1,num+1):
    # another for loop for columns 
    for j in range(1,i+1):
        print("*", end=" ")
    print()
    

#  pattern in reverse
for i in range(num,0,-1):
    # another for loop for columns 
    for j in range(1,i+1):
        print("*", end=" ")
    print()

# pattern in right angle 
for i in range(1,num+1,+2):
    # another for loop for columns 
    for j in range(1,i+1):
        print("*", end=" ")
    print()

# pattern 

n= int(input("enter the number of rows: "))
m=(n+1)*n//2
for i in range(n):
    for j in range(i+1):
        print(m, end=" ") 
        m-=1
    print()