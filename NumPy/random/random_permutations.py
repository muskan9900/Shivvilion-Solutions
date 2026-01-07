""" random permutations """
# to perform permutation the random module has two methods shuffle() and permutation()

from numpy import random
import numpy as np

# shuffling  Arrays
# changing arrangements of elements in the array itself 
# the shuffle() method makes changes to the original array 

arr=np.array([1,2,3,4,5])
random.shuffle(arr)

print(arr)
print("the og:array",arr)

# generating permutation of arrays 
# using permutation method 
# the permutation() method returns a re-arranged array 
# leaves the original array unchanged 

arrp=np.array([1,2,3,4,5,6])
print(random.permutation(arrp))
print("the og:array",arrp)