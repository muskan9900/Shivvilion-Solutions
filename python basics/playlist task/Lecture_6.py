""" Lecture 6 Funcion and Recursion """

#  creating a basic function with example

def calc_sum(a,b): # parameters
    return a+b
sum=calc_sum( 12,13) # argumets , call of function
print(sum)  

#  to create multiple task with no parameters 

def print_hello():
    print("hello")

print_hello() # first time the function is called
print_hello() # second time function is called


# calculating the average of 3 numbers 

def calc_avg(a,b):
    avg= a+b/2
    return avg

total=calc_avg(12,13)
print(total)

"""  types of function built in function
    1. built in functions
    2. user-defined functions
 """

""" default parameters """

