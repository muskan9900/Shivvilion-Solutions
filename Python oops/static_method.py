""" oops concept """

""" static method """

# time 27min
# methods that dont use self paramter
# works at class level
#  to use static method @decorator is used 
 


class Dog:
    species="canine"

    @staticmethod
    def hello():
        print("Greetings,Good Morning")

    def __init__(self,name,age):
        print(self)
        self.name=name
        self.age=age


#  creating a object 
Dog1=Dog("buddy",32)
print(Dog1)

# print(Dog1)
print(Dog1.name)
print(Dog1.species)
print(Dog1.age)

# object 2 created
Dog2=Dog("charlie",22)  
print(Dog2.name,Dog2.age)
print(Dog2)

Dog1.hello()
