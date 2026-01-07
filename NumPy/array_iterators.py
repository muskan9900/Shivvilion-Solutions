import numpy as np

arr=np.array([1,2,3,4,5])

# iterating through elements of array by using for loop
# basic way to iterate using for loop in 1-D 
 
for x in arr:
    print(x)

# similar way iterating through 2-D 

arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])

for x in arr2:
    print(x)

# to return more actual values following is method to iterate
# this goes through each element and print the value properly
for x in arr2:# x takes each list
    for y in x: # y takes each element from the list 
        print(y)

# iterating over 3-D array

arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in arr3:
    print(x)

# print each value of 3-D array

for x in arr3:
    for y in x:
        for z in y:
            print(z)

#  using ndtier()
# this more easier way to print than printing with basic loops
# basic loops are okay but when dimension are higher , its difficult to write n loops

arr4=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in np.nditer(arr4):
    print("the ndtier function:",x)

# iterating array with different data types

# the original data type of array cant be changed while iterating so extra space is used 
# that extra space is the buffer (temporary space)
# we are allow to use that buffer , flags=['buffered']
# 

arr=np.array([1,2,3])
for x in np.nditer(arr,flags=["buffered"],op_dtypes='S'):
    print(x)

# iterating with different step size 
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in np.nditer(arr[:,::2]): # [:,::2] 
                                # : is for row
                                # : : 2 for coloumns just like slicing 
    print(x)

# enumerated iteration 
# done by using ndenumerate()
# Enumeration means getting both the position (index) and the value together.

arr=np.array([1,2,3])
for idx , x in np.ndenumerate(arr):
    print(idx,x)