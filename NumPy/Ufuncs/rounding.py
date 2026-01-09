""" rounding decimals """

# 5 ways of rounding in decimals
        # truncation
        # fix
        # rounding
        # floor
        # ceil

import numpy as np

# truncation
# by trunc()
# Remove the decimals, and return the float number closest to zero

arr=np.trunc([-3.16666,3.6667])
print(arr) # output is -3. 3.

# fix
# by fix()
#  fix is same as truncate 
# fix deprecated
arr=np.fix([-3.16666,3.6667])
print(arr) # output is -3. 3.

# rounding
# by around()
arr=np.around(3.6666,2)
print(arr)

# floor()
arr=np.floor([6.77777,8.27277272])
print(arr) # [6.,8.]
# rounds to nearest lowest integer

# ceil() 
arr=np.floor([6.77777,8.27277272])
print(arr) # rounds to nearest upper integer

