""" generating random number  """
""" NumPy offers random module to work with random numbers """

from numpy import random 

x=random.randint(100)
print(x)

# generating random float 
#  rand() is used to generate float between 0 and 1 

x=random.rand()
print(x)

# generating arrays from random module 
# creating random array with integers using randint() and size as parameter 
#  size is the shape of arrays 

# generating a 1-D array
arr=random.randint(100, size=(5)) 
print(arr)

# genrating a 2-D array

arr2=random.randint(100,size=(2,3))
print("the 2-d array with random int:",arr2)

# generating array using rand() , it generates float number along with specifying 
# the shape of array 

# generating 1-D array
arr4=random.rand(3)
print("the random floated 1-D array with floated number:",arr4)

# generating 2-D array
arr5=random.rand(3,5)
print("the random floated 2-D array with floated number:",arr5)

# generating random Number from array 
# using choice()
x=random.choice([3,5,7,9])
print(x)

