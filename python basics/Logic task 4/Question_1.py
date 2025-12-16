""" Shop Bill Calculator
Scenario:
 A small shop wants to calculate the total bill.
Task:
Take price of 3 items
Calculate:
    Total amount
    5% discount if total > 1000
    Final payable amount
 """
#  time taken 30 min 

def calculate(total_amt):

    if total_amt>1000:
        discount=5
        discounted_amount=(discount/100) * total_amt
        final_payable=total_amt-discounted_amount
        return final_payable

    else:
        print("no discount avaible")

#  user in put
item1=float(input("price of item 1: "))
item2=float(input("price of item 2: "))
item3=float(input("price of item 3: "))

total_amt =item1+item2+item3
print("the total amount",total_amt)
result=calculate(total_amt)
print("the discounted amount",result)





