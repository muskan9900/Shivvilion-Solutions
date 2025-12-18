""" question 1 """

class student:

    def __init__(self,name,marks):

        self.name=name
        self.marks=marks

        print(f"the name of student: {self.name}")
        print(f"the marks of 3 subjects:  {self.marks}")
      

    def calculate_average(self):

        sum=0
        for val in self.marks:
            sum+=val
        print(f"Hello {self.name}, your average score is: {sum//3}")



#  creating objects and passing marks to the name of the student

s1=student("williams",[33,45,67])
s2=student("Jhon",[89,78,54])
s3=student("Charlie",[34,56,90])

s1.calculate_average()
s2.calculate_average()
s3.calculate_average()
        