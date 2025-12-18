""" oops concept """

"""  class variable and instance variable  """

#  time 26min
# class variable are used by the all objects
# declared at  class level , outside any method 
# class variable share the same value for all the objects 

# instance varible 
# variable that are unique to each object created 
# defined within the __init__ method 
#  each objects maintains its copy of instance variable 


class Dog:
    species="canine"

    def __init__(self,name,age):
        self.name=name
        self.age=age

#  creating the object 

dog1=Dog("buddy",32) 
dog2=Dog("charlie",44)

print(dog1.name,dog1.age)
print(dog2.name,dog2.age)
print(dog1.species)

# modifying instance variable 

dog1.name="Max" # only dog1 is modified it wont effect other objects , maintains own instance variable
print(dog1.name)

# modifying class varibale 

Dog.species="faline"
print(Dog.species) # class varible printed with modification
print(dog1.species) # dog1 value changes as class varible is modified 
print(dog2.species) # holds same value of class variable as dog1 hold no change same for every object


    
