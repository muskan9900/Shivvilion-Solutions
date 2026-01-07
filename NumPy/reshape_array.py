import numpy as np
# reshaping the array from 1-D to 2-D
# by using reshape() we can shape the array
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
rs=arr.reshape(4,3)
print(rs)

#  reshaping from 1D to 3D 
arr1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
rs1 = arr1.reshape(2, 3, 2)
print(rs1)


# to check the base of the reshaped array 

arr2=np.array([1,2,3,4,5,6,7,8])
print(arr2.reshape(2,4).base) # this returns a view , so its a original array 

# unknown dimension 
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2,-1)

print(newarr)

# flattering the arrays 
# converting the multidimensional array into 1D 

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
new=arr.reshape(-1) # -1 makes its 1D array
print(new)
