""" exceptional handling example with try and except """

#  try is the block where the error is expected
# except returns the error on output when it is found in try block 

n=10

try:
    res=n/0

except ZeroDivisionError:
    print("Cant divide by zero ")

#  knowing the difference between error and exception

# error that is serious and logical problem that cant be handled

print("missing paranthesis") 
#  missing paranthesis


# exception zerodivision exception
n=10
res=n/0


