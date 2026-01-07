import numpy as np

arr1=np.array([1,2,3,4,5,6,7])

print(arr1[1:5]) # last index is not included 

#  slice from the beggining
print(arr1[:5]) # start not specified it considers 0 from start 

print(arr1[1:]) # end not specified considers the length of array

print(arr1[-5:-1]) 
print(arr1[-3:-1])

#  using step in slicing

arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])
print(arr[::2])

# slicing of 2-D array 

