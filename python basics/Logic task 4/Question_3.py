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

    if (units==1 or units==100):
        calc= units*3
        total=calc*30 # 30 = number of days in a month

        return total
       
    elif( units==100 or units==200):
        calc= units*5
        total=calc*30 # 30 = number of days in a month

        return total
        
    elif units>=200:
        calc= units*7
        total=calc*30 # 30 = number of days in a month 
        return total
    
    else:
        print("units out of range")
   
# user input
units=float(input("enter the number of units consumed: "))
print("total number of units:",units)
total_bill=calculate_units(units)
print("the total bill",total_bill)



    



