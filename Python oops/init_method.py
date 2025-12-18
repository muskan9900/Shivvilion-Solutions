""" oops concept """

""" # __init__ method  """

#  time 14 min

# it is constructor called automatically when object is created 
# its allows us to access the attributes for each object created 
#  a special method used for initialization


class Dog:
    species="canine"

    def __init__(self,name,age):
        self.name=name
        self.age=age

#  creating objects 

Dog1=Dog("buddy",32)

print(Dog1.name)

