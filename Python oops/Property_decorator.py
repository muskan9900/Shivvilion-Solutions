""" oops concept """

""" property decorator"""

# time 35min

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy+self.chem+self.math)//3)+"%"


    #  creating another method to change the percentage 
    # the percentage will change for the subject marks changed

    # def calculate_percent(self):
    #    self.percentage=str((self.phy+self.chem+self.math)//3)+"%"
    #    print(self.percentage)

    """ by creating a method that changes a attribute,  
    this can be done by property decorator""" 
    # property decorator converts the function into attributes
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)//3)+"%"
    

stu1=Student(30,97,99)
# print(stu1.percentage)   
#  print(self.percentage)

# suppose to change the value of a paticular subject

stu1.phy=23
print(stu1.phy)

# but now print the percent after changing the subject
print(stu1.percentage) # it prints the same
# stu1.calculate_percent() # this prints the changed marks subject percentage


