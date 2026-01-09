""" binomial distribution """
# it has two values eg tossing a coin has two values head or tail
# random.binomial() is used 
# n - number of trials.

# p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).

# size - The shape of the returned array.

from numpy import random

x=random.binomial(n=10,p=0.5,size=10)
print(x)