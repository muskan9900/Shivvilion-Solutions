""" oops concept """

# time 20 min

""" # self parameter """

# it is a reference to the current instance 
#  it allows us to access the attributes and methods of the object 

class Dog:
    species="canine"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    
Dog1=Dog("buddy",32)
Dog2=Dog("charlie",42)

print(Dog1.name,Dog1.age,Dog1.species) # accessing class and instance attributes through object 1
print(Dog2.name,Dog2.age,Dog2.species) # accessing class and instance attributes through object 2 
print(Dog.species) # directly accessing the class attribute

    
