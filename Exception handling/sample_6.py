""" custom exception handling """

class AgeError(Exception):
    pass
def set(age):
    if age <0:
        raise AgeError("age cannot be negative")
    print(f"age set to {age}")

try:
    set(-5)
except AgeError as e:
    print(e)
