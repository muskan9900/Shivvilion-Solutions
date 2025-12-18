""" practice que  """

# time 31 min

class Account:

    def __init__(self,balance,account):
        self.balance=balance 
        self.account=account
        
    # debit method
    def debit(self,amount):
        self.balance-=amount
        print(f"the amount {amount} was debited from the {self.account}")
        print("The total balance in your acc is:", self.get_bal())
    
    # credit method
    def credit(self,amount):
        self.balance+=amount
        print(f"the amount {amount} is credited to {self.account}")
      
        print("The total balance in your acc is:", self.get_bal())
    # printing method
    def get_bal(self): 
        return self.balance
        
    
# creating objects

a1=Account(10000, "123acc")
print(a1.balance)
print(a1.account)

a1.debit(2000)
a1.credit(1000)
a1.get_bal()





    