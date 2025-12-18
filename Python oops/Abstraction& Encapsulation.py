"""oops concept"""

""" Abstraction """

# time 32 min

""" hiding the implementation details of a class and 
and only showing the essential features to the user """ 

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
            self.clutch=True
            self.acc=True
            print("car started")

#  creating objects
car1=Car()
car1.start()

"""oops concept"""

""" Encapsulation"""

# time 6 min
# wrapping data and functions into single unit (objects)
 
