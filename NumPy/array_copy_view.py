import numpy as np

# creaing copy of array and checking that it affects the original array 
arr=np.array([1,2,3,4,5])
x= arr.copy()
x[3]=66
print("the copied array:",x) # [1,2,3,66,5]
arr[0]=55
print("the original array:",arr) #[55,2,3,4,5]

# creating view of array and checking that it affets or not the original array

arr=np.array([1,2,3,4,5])
v=arr.view()
print("the view of array:", v)
arr[0]=88
print("the view of array with value changed:",v)
print("the original array:",arr)
v[2]=77
print("the view of array with value changed:",v)
print("the original array:",arr)

