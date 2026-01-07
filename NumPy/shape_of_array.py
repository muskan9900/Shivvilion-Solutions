import numpy as np

arr=np.array([1,2,3,4,5])
# the shape of array refers to number of elements in each dimensions
#  it uses the shape attribute to return the shape of array 
print(arr.shape) # it returns a tuple with each index

arr2=np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr2.shape)

# creating an array with ndmin and checking its shape

arr3=np.array([1,2,3,4,5], ndmin=5)
print(arr3)
print(arr3.ndim)
print("the shape of the array:",arr3.shape)