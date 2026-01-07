""" data distribution  """
# list of all possible values and how often each value occurs
""" # random distribution """
# a set of random numbers that follows a certain probability density function
# probability density function , a function that describes a continous probability 
# probability of all values in an array 

# choice method allows to specify the probablities for each values
# probability is set by 2 numbers 0 and 1 
# 0 means value will never occur 
# 1 means value will always occur 


""" Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

        The probability for the value to be 3 is set to be 0.1

        The probability for the value to be 5 is set to be 0.3

        The probability for the value to be 7 is set to be 0.6

        The probability for the value to be 9 is set to be 0 """

from numpy import random
p=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(100))
print("1-D array:",p)

# same example but it returns 2-D array 

p2=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(3,5))
print("2-D array:",p2)