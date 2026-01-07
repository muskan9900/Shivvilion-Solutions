import numpy as np
# dtype attributes returns the data type of the array 

arr=np.array([1,2,3,4,5])
print("the data type of arr is :", arr.dtype)

#  array with strings

arr=np.array(["apple","kiwi","mango"])

print("the datatype of array is :", arr.dtype)


# creating arrays with defined data type 
# using dtype as arguments

arr=np.array([1,2,3,4,5], dtype='S')
print(arr)
print(arr.dtype)

arr=np.array(['1','2','3','4','5'], dtype='i')
print("the string converted array:",arr)
print(arr.dtype)

# size can also be define along with defined data type
# this has an array data type with 4 bytes integer
arr=np.array([1,2,3,4,5], dtype='i4')
print("the array with 4byte integer",arr)
print(arr.dtype)

# changing the data type 
#  here the conversion is from float to integer by using int parameter 

arr=np.array([1.1,1.2,1.3])
print(arr)
print("the float value:" , arr.dtype)

# using astype() we change the data type 
new_Arr=arr.astype(int)
print(new_Arr)
print("the int value of arr is :", new_Arr.dtype)

# changing the data type to boolean

arr=np.array([1.1,1.2,1.3])
print(arr)
print("the float value:" , arr.dtype)

# using astype() we change the data type 
# here boolean is used
new_Arr=arr.astype(bool)
print(new_Arr)
print("the int value of arr is :", new_Arr.dtype)
