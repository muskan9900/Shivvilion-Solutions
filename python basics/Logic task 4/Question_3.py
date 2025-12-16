""" Electricity Bill Calculator
Scenario:
 Calculate monthly electricity bill.
Task:
    Take units consumed
Charges:
    First 100 units → ₹3/unit
    Next 100 units → ₹5/unit
    Above 200 units → ₹7/unit
Print total bill 
"""
# time taken 25 min
def calculate_units(units):

    if units<=100:
        total= units*3

    elif units<=200:
        total=100*3 + ((units-100)*5)

    else:
        total=(100*3)+ (100*5)+((units-200)*7)
    
    return total
    
# user input
units=float(input("enter the number of units consumed: "))
print("total number of units:",units)
total_bill=calculate_units(units)
print("the total bill",total_bill)



    



