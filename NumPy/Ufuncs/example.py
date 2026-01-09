""" ufunc """
# ufunc are universal function , performed on ndarray
# ufuncs are used to implement vectorization in NumPy which is way 
#   faster than iterating over elements.
# vectorization:
# converting the iterative statements into vector based operation is called vecttorization

# a example without ufuncs
#  without ufuncs , zip() is used

x=[1,2,3,4]
y=[4,5,6,7]
z=[]

for i,j in zip(x,y):
    z.append(i+j)
print(z)

# NumPy has a ufunc called add(x,y), which does the same as above

import numpy as np

x=[1,2,3,4]
y=[4,5,6,7]
z=np.add(x,y)
print(z)

