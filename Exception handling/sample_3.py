""" working with specific exceptions  """
# specific exception help us to debug where the error is
# following is the demonstration

# 1) catching specific exception

try:
    x=int("str") # this will cause the value error 
    inv=1/x # inverse calculation 

except ValueError:
    print("not valid ")

except ZeroDivisionError:
    print("zero has no inverse")

# ----- second specific condition----#

try:
    x=int("0") # this will cause the value error 
    inv=1/x # inverse calculation 

except ValueError:
    print("not valid ")

except ZeroDivisionError:
    print("zero has no inverse")
# this return the zerodivision error