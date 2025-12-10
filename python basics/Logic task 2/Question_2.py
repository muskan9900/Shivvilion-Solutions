
#time started at 9:45 am to 10:30pm
# to count vowels 
#takes a string and return the number of vowels(a,e,i,o,u)

# taking user input 
user_str= input("Enter your text:")
print(user_str)

# a string for vowels 
vowels= "aeiouAEIOU" 

count=0 # a counter variable

# initializing a for loop
for c in user_str:
    if c in vowels:
        count +=1
print(count)






    


    
    