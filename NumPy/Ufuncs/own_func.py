""" creating own ufunc  """

# STEP 1 creating normal fun
# STEP 2 adding it to NumPy ufunc library with frompyfunc() 
# STEP 3 frompyfunc() this has 3 parameters
        # function - the name of the function.
        # inputs - the number of input arguments (arrays).
        # outputs - the number of output arrays.

# creating functions
import numpy as np

def myadd(x,y):
    return x+y

myadd=np.frompyfunc(myadd,2,1)

print(myadd([1,2,3,4,5],[4,5,6,7,9]))


# checking the type of function , if it is a ufunc or not
print(type(np.add))

# print(type(np.blablaj)) -> shows error becuase such methods dont exit in numpy



