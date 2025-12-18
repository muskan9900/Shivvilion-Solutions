""" oops concpet """

""" Super()  """

#  time 21 min

""" super() method is allowed the child
 class to access
 the parent class method""" 

class C:
    def __init__(self,order):
            self.order=order


class B(C):
      
      def __init__(self,greet,order):
            self.greet=greet
            super().__init__(order)

b1=B("good morning","reverse",)
print(b1.order)
print(b1.greet)

            
            