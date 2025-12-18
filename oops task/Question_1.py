""" Create a payroll management system using OOP.
Requirements:
     Create a base class Employee with attributes:
     name, emp_id, base_salary
Create subclasses:
      FullTimeEmployee
      ContractEmployee
Salary rules:
        Full-time employee → base_salary + bonus (10%)
        Contract employee → base_salary * hours_worked
Create a class PayrollSystem that:
              Stores multiple employees
              Calculates monthly salary for each
Displays salary slip in clean format """

class Employee:

    def __init__(self,name,emp_id,base_Salary):
     self.name=name
     self.emp_id=int(emp_id)
     self.base_Salary=int(base_Salary)
     self.total_salary= 0


class FullTimeEmplyoee(Employee):
   
   def calculate_salary(self):
        bonus = self.base_Salary * 0.10
        self.total_salary = self.base_Salary + bonus

   def display(self):
          print(f"ID: {self.emp_id}")
          print(f"Name: {self.name}")
          print("Type: Full-Time")
          print(f"Total Salary: {self.total_salary:.2f}")
          


class ContractEmployee(Employee):

     def __init__(self, name, emp_id, base_Salary, hours_Worked):
     #     super() calls the parent class constructor
         super().__init__(name, emp_id, base_Salary)
         self.hours_Worked= hours_Worked
# base_salary is consider the pay for 1 hour 
# 1 hours= base salary
     def calculate_Salary(self,hours_worked):
       
       self.total_salary= self.base_Salary*hours_worked

     def display(self):
          print(f"ID: {self.emp_id}")
          print(f"Name: {self.name}")
          print("Type: Contract Type")
          print(f"Hours Worked: {self.hours_Worked}")
          print(f"Total Salary: {self.total_salary:.2f}")
          
   
# class PayrollSystem:

#     def calculate_monthly_salary(self):



# creating objects 
t=Employee("sarah",1,3000)
print(t.name)
print(t.emp_id)
print(t.base_Salary)

t2=FullTimeEmplyoee("john",2,45987)
print(t2.name)
print(t2.emp_id)
print(t2.base_Salary)

t2.calculate_Salary()

# # contract salary 

# t3=ContractEmployee("williams",1,8000)
# print(t3.name)
# print(t3.emp_id)
# print(t3.base_Salary)

# t3.calculate_Salary(6)
