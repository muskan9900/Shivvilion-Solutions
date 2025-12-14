""" Lecture 5 Loops  """

""" practice question  """
# Q1 
# i= 1

# while i<= 100:
#     print(i)
#     i +=1

# Q2 
 
# i= 100

# while i>=1:
#     print(i)

#     i-=1

# Q3 

# i=1 
# n=int(input("enter the number: "))

# while i<=10:
#     print(n*i)
#     i+=1

# # Q4

# x=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index=0
# while index<len(x):
#     print(x[index])
#     index += 1

# Q5
# nums=(1,4,9,16,25,36,49,64,81,100)

# index=0 

# x=49

# while index<len(nums):
#         if(nums[index]==x):
#                 print("Found", index)
#         else:
#                 print("finding")
#         index +=1

# break and continue keywords
# break keyword is used to terminate the loop when condition is satiesfied 
# continue keywords 
# it terminates the current iteration & continues the execution of the loop with the next iteration 
# i= 1 

# while i<=10:
#     if i==3:
#         i+=1   
#         continue 
#     print(i)
#     i+=1

# for loops 

# List=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 


# for x in List:
#     print (x)

#   range function
# generally used in all terms 
#  it includes terms like start which is by default zero
#  step by default an increament of one
# stop compulsory

""" example of range """

""" for i in range(5): # stop
    for i in range(2,5) :# start, stop
        for i in range(2,3,1): # start stop step
 """

# # q 1
# for i in range(1,101):
#     print(i)

# # q2 
# for i in range(100,0,-1):
#      print(i)

# q3 

# n=int(input("enter the number:"))

# for i in range(1,11):
#     print(i*n)


""" pass statements """

#  pass statement

#  working of sample

# for i in range(5):
#     pass  
# print("some useful work")


""" question """

# q1

n= 100

sum = 0

i= 1

while i<=n:
    sum+=i
    i+=1
print(sum)
    
""" way to print for loop """

# for i in range(1,n+1):
#     sum += i
# print("the total sum is:", sum )

# Q2

""" to calculate factorial """

n= 5
fac=1

for i in range(1,n+1):
    fac*=i
print(fac)







 

