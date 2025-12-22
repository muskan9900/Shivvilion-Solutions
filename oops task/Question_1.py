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
     self.emp_id=emp_id
     self.base_Salary=int(base_Salary)
     
    def Calculate_Salary(self):
     #    calculates the salary for the employee
     raise NotImplementedError("Subclasses must implement this method")
    
    def __str__(self):
           return f"{self.name} ({self.emp_id})  ₹ {self.base_Salary}"
     
class FullTimeEmplyoee(Employee):
     def __init__(self, name, emp_id, base_salary, bonus_rate=0.10):
        super().__init__(name, emp_id, base_salary)
        self.bonus_rate = bonus_rate

     def Calculate_Salary(self):
          #  full time employee salary: base salary * 10%
               bonus = self.base_Salary * self.bonus_rate
               return self.base_Salary + bonus
               


class ContractEmployee(Employee):

               def __init__(self, name, emp_id, base_Salary, hours_Worked):
               #     super() calls the parent class constructor
                    super().__init__(name, emp_id, base_Salary)
                    self.hours_Worked= hours_Worked
          # base_salary is consider the pay for 1 hour 
          # 1 hours= base salary
               def Calculate_Salary(self):
                    return self.base_Salary*self.hours_Worked    
               
   
class PayrollSystem:
     "manages employee and calculates their payroll"

     def __init__(self):
     # creating a list for storing employees
          self.employees=[]
     
     def add_employee(self,employee):
     # adds the employee to the list 
      self.employees.append(employee)

     def calculate_payroll(self):
     #  calculates the monthly salary for all employees.
#      """ This is polymorphism (OOP concept):
     
# If employee is a FullTimeEmployee, Python runs FullTimeEmployee.Calculate_Salary()

# If employee is a ContractEmployee, Python runs ContractEmployee.Calculate_Salary() """
          print("#"*10)  
          print(            "MONTHLY PAYROLL REPORT"                                       )
          for employee in self.employees:
               salary=employee.Calculate_Salary()
               self.display_salary_slip(employee,salary)
          print("#"*10)   

     def display_salary_slip(self,employee,salary):
          print("#"*10)  
          print(f"Employee ID:{employee.emp_id}")
          print(f"Employee Name: {employee.name}")
          print(f"Base Salary:{employee.base_Salary}")
          if isinstance(employee,FullTimeEmplyoee):
               print(f"Base Salary:   INR {employee.base_Salary:,.2f}")
               print(f"Bonus (10%):   INR {employee.base_Salary * employee.bonus_rate:,.2f}")
          elif isinstance(employee, ContractEmployee):
               print(f"Hourly Rate:   INR {employee.base_Salary:,.2f}")
               print(f"Hours Worked:  {employee.hours_Worked}")

          print(f"Total salary: INR {salary}")
          print("#"*10)  

# creating employees and adding the list 

# creating the employess
ft_emp=FullTimeEmplyoee("Sarah","FT001",4000)
ct_emp=ContractEmployee("Williams","CT001",5000,7)

# initializing the payroll system 

Payroll_system=PayrollSystem()

# adding employees to the payroll
Payroll_system.add_employee(ft_emp)
Payroll_system.add_employee(ct_emp)
Payroll_system.calculate_payroll()


# oops concept used
# 1. class objects
# 2.encapsulation
# 3. polymorphism
# 4. inheritance
# 5.method overriding

  


