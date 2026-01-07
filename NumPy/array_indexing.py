import numpy as np

# arr=np.array([1,2,3,4])
# print("the first element of array:",arr[0])
# print("the second element of array:",arr[1])
# print("the third element of array:",arr[2])
# print("the addition of two elements of array:",arr[2]+arr[3])

# accessing 2-D array elements

arr2=np.array([[1,2,3,4],[2,3,4,5]])
print("2nd element from 1st row:", arr2[0,1])

# accessing the 3-D array elements

arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("the third element of second array from first array is:" , arr3[0,1,2])

# negative indexing 

arr4=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print("the last element from 2nd dimension is:" ,arr4[1,-1])


 
