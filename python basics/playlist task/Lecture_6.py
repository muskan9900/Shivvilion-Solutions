""" Lecture 6 Funcion and Recursion """

#  creating a basic function with example

# def calc_sum(a,b): # parameters
    # return a+b
# sum=calc_sum( 12,13) # argumets , call of function
# print(sum)  

#  to create multiple task with no parameters 

# def print_hello():
#     print("hello")

# print_hello() # first time the function is called
# print_hello() # second time function is called


# calculating the average of 3 numbers 

# def calc_avg(a,b):
#     avg= a+b/2
#     return avg

# total=calc_avg(12,13)
# print(total)

"""  types of function built in function
    1. built in functions
    2. user-defined functions
 """

""" default parameters """

"""b=2 are default values only passing a as args
 first parameter should be an default argument following 
 second argument as well ,if a has default value b cant be empty , 
 but a can be empty having b as default value  
"""

# def calc_num(a,b=2): 

#     print(a*b)
#     return a*b

# calc_num(3)

""" Prcatice set """
    
# Q 1 

# list=[10,20,29,34]

# def len_list(list):
#     print(len(list))
#     return list

# len_list(list)

# Q 2

# def el_list(list):
#     for i in list:
#         print(i, end=" ")

# el_list(list)


# Q 3

# n=int(input("enter the number of n: "))


# def fact_n(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#         print(fact)

# fact_n(n)


# Q4

#  WAF to convert USD to INR

#  1$ equals to 83 rupess


# usd=int(input("enter the usd: "))
# def conversion(usd,inr=83):
#     n=usd*inr
#     print(usd ," usd value =", n,"inr value ")

# conversion(usd)

#  program 

# num=int(input("enter the number: "))

# def check(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# check(num) 

""" recursive functions """

# def show(n):
#     if (n==0): # a condition to stop is called base case
#         return 
#     #  if base is removed just like loops recursion works infinitely
#     print(n)
#     show(n-1)
#     print("end")

# show(5)

""" recursive function of any n factorail numbers """

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return fact(n-1)*n
# print(fact(1))

""" practice question """

# Q 1

# def natural_num(n):
#     if n==0:
#         return 0
#     return natural_num(n-1)+n

# sum=natural_num(5)
# print(sum)

# Q 2 


def print_list(list,indx):
    if(indx==len(list)):
        return
    print(list[indx])
    print_list(list,indx+1)

fruit=["mango","banana","apple","pineapple","kiwi"]

print_list(fruit,0)

    


        
                   



 