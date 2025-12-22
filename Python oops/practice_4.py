""" practice question """

class Employee:

    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    

    # creating a method
    def show_details(self):
        print( "role = ", self.role)
        print("dept= ", self.dept)
        print("salary= ", self.salary)


class Engineer(Employee):
    def __init__(self,name, age):
        self.name=name
        self.age=age
        super().__init__("Engineer",  "IT","75000")
    
    def show_details(self):
        print("name=",self.name)
        print("age=",self.age)
        return super().show_details()
        

eng1=Engineer("Rahul",34)
eng1.show_details()