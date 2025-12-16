""" Mobile Recharge Calculator
Scenario:
 A user recharges their mobile balance.
Task:
    Take recharge amount
Add:
10% extra talktime if recharge ≥ 199
Show final balance
 """
#  time taken 18 minutes 
def calculate_balance(result):
    if result>= 199:  # result = recharge_amt
        extra=10

        talk_time=(extra/100)*result
        total= result+talk_time
        return total
    else:
        print("no extra talk time ")

#  user input 
recharge_amt=float(input("enter the recharge amount: "))
result=recharge_amt
print("the recharge amount",result)
final_bal=calculate_balance(result)
print("the final balance",final_bal)