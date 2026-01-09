import numpy as np

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])

# newarr = np.add(arr1, arr2)

# print(newarr)

#  summation 

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)

# axis=1 it will sum the numbers in each array 
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)
