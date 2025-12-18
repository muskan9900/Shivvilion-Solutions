""" oops concpet """

""" class method  """

#  time 44min

"""class method are used to  modify the class
 attributes directly using @ class decorator""" 

class Person:
    name="anonymous"

    # #  without using the class decorator
    # def ChangeName(self):
    #     self.__class__.name="Rahul"

    # general way to change 

    # def change(self,name):
    #     self.obj=name
    """ here the name 
    attribute of the class doesnt change
    a new obj attribute is changes that is the 
    instance attribute
    class attribut remains the same"""

    # way to change class attribute using class method
    # using class decorator
    # just like self use cls as parameter

    @classmethod
    def ChangeName(cls,name):
        cls.name=name

# creating objects

p1=Person()
p1.ChangeName("rahul")
print(p1.name)
print(Person.name)

# p1.change("rahul j")
# print(p1.obj)
# # p1.ChangeName()
# print(p1.name)