""" catching multiple exception  """
# the following program perform multiple exception in a 
# single try block
# doubt requires more value change 

a=["10","twenty",30]

try:
    total=int(a[0]+int(a[1])) # "twenty" cannot be converted to int

except (ValueError,TypeError) as e:
    print("Error",e)

except IndexError:
    print("index out of range.")


