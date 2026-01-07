import numpy as np

# dimensions in arrays is one level of array depth (nested arrays)

# create a 0-D array with values 42

arr=np.array(42)
print("its 0-D array",arr)

# create a 1-D array containing the values 1,2,3,4,5

arr2=np.array([1,2,3,4,5])
print("its 1-D array",arr2)

# create a 2-D arrays 
# 2-D means 1-D arrays as its elements

arr3=np.array([[1,2,3,4],[5,6,7,9]])
print("its 2-D array",arr3)

# create a 3-D arrays
# a 3-D array has 2-D arrays as its elements

arr4=np.array([[[1,2,3,4],[4,5,6,7]],[[2,3,4,5],[7,8,9,6]]])
print("its 3-D array",arr4)

# checking the number of  dimensions 
# ndim attribute that returns an integer , tell how many dimensions an array has

a=np.array(42)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3,4],[5,6,7,9]])
d=np.array([[[1,2,3,4],[4,5,6,7]],[[2,3,4,5],[7,8,9,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# checking if a paticular program has 5 dimensions or not 
# an array can have any number of arguments, it is define by the ndmin 

arr=np.array([1,2,3,4],ndmin=5)

print(arr)
print('number of dimensions:', arr.ndim)
