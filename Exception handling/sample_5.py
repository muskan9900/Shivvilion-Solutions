""" raising an exception """
# using by raise keyword
# followed by the instance of exception type from built in Exception class
# or from creating custom exception by inheriting the Pythons built in exception class

def set(age):
    if age<0:
        raise ValueError("age cannot be negative")
    print(f"age set to {set}")

try:
    set(-2)

except ValueError as e:
    print(e)
