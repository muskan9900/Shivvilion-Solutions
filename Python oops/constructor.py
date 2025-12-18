""" oops concept """

""" constructor  """

class A:

    # # defualt constructor
    # def __init__(self):
    #     pass

    # parameterized constructor 
        def __init__(self ,name ,age):
            self.name=name
            self.age=age
            print("student in database")


# creating objects

obj1=A("heelo",32)
print(obj1.name)
print(obj1.age)

