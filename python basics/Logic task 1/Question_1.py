    # a program to check the final payable amount


def calculating_final_amount(amount):
    
    if amount>1000:
        discount_percentage=10
    else:
        discount_percentage=5
    discounted_amount=(discount_percentage/100) * amount
    total_amount= amount -discounted_amount
    return total_amount
  

# taking the user input 
purchased_amount= float(input("Enter the purchased amount:"))

# calculationg the final amount

final_payable= calculating_final_amount(purchased_amount)
print(f"the purchased amount{purchased_amount: .2f}")
print(f"print the payable amount{final_payable:.2f}")
