""" normal data distribution """
# random.normal() for normal data distribution
#  it has three parameter
# loc -(Mean)
# scale - (Standard Deviation)
# size - The shape of the returned array.

from numpy import random

x=random.normal(size=(2,3))

print(x)

# using the parameters
x=random.normal(loc=1,scale=2, size=(2,3))