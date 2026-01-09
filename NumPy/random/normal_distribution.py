""" normal data distribution """
# random.normal() for normal data distribution
#  it has three parameter
# loc -(Mean)
# scale - (Standard Deviation)
# size - The shape of the returned array.

from numpy import random

x=random.normal(size=(2,3))

print(x)

# # using the parameters
x1=random.normal(loc=1,scale=2, size=(2,3))
print(x1)

# visualization 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde")

plt.show()