""" exception handling with 4 main keywords  """
# try :coantains the risky code
# except: throws error if catched in try
# else: it runs when no error in the try block
# finally: run no matter what happens for clean look

try:
    n=10
    res= n/0

except ZeroDivisionError:
    print("division by zero is not possible ")

# adding one more exception

except ValueError:
    print("enter a valid number!")

else:
    print("the result is ",res)

finally:
    print("execution completed")
