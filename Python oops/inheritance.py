""" oops concept """

""" Inheritance """

#  time  1 hour
""" # it is concept that allows child class to acquire 
 properties and methods of another class(parent class) """

# promotes code reuseability 
# supports heirarchical classification

""" Types of Inheritance:
1.Single Inheritance: A child class inherits from a single parent class.

2.Multiple Inheritance: A child class inherits from more than one parent class.

3.Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.

4.Hierarchical Inheritance: Multiple child classes inherit from a single parent class.

5.Hybrid Inheritance: A combination of two or more types of inheritance. """


# class dog is parent class
class Dog:
    def __init__(self,name):
        self.name= name 

    def display_name(self):
        print(f"Dog's Nmae: {self.name}")

# SIngle level inheritance 
# child class Labrador inehrits parent class Dog 
class Labrador(Dog): 
    def sound(self):
        print("Labrador woofs")

# multilevel inheritance
# labrador inherits from Dog
# guidedog inherits the inherited class labrador
class GuideDog(Labrador):
    def guide(self):
        # self.name is present in the parent class dog
        # GuideDog can access becuase it is inherited from Labrador
        # where Labrador has properties and methods of Parent dog class
        print(f"{self.name} Guides the way!")

# multiple inheritance
class Friendly:
    def greet(self):
        print("friendly!")

class GoldenRetriever(Dog,Friendly): #multiple inheritance 
    def sound(self):
        print("Golden retriever Barks")


# example usage 

lab=Labrador("buddy")
lab.display_name() # parent class method invoked through child class
lab.sound() # child class method called

guido_dog= GuideDog("Max")
guido_dog.display_name()
guido_dog.guide()

retriever=GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()



