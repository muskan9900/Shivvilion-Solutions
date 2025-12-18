""" oops concept """

#  time 40 min 

""" # class  """
# class is created  with class keyword
# class has set of attributes and method that a object can have
# class are collection of objects
# class are blueprints for creating objects
# attributes are the variables of the class they are public and can be accessed by .operater 
#  eg MyClass.My attributes 

""" creating a class """

class Dog: # dog is the name of class , class keyword indicates creating a class
    species="canine" # attributes or variable of class Dog

    def __init__(self,name,age):
        self.name="name" # instance attribute
        self.age="age"   # instance attribute

#  __init__ method = initializez the name and age attributes when a new object is created 