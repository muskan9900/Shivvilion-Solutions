""" oops concept  """

""" ploymorphism """

# time 


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real ,"i +", self.img ,"j")
    
    # normal way to add 
    # def add(self,num2):
    #     newReal=self.real+num2.real
    #     newImg=self.img+num2.img
    #     return complex(newReal,newImg)

    # similar way to add as dunder function
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return complex(newReal,newImg)




num1= Complex(10,4)
num1.showNumber()

num2= Complex(13,8)
num2.showNumber()

# num3=num1.add(num2)
# num3=showNumber()

# after adding dunder function we can 
num3=num1+num2
# num3.showNumber()
 

 

