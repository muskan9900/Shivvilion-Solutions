
# started at 10:30pm to 11:30 pm
# write a program to print all unique number from given list (number that appear only at once )

numbers=[1,2,3,2,5,3,7,9]

unique_numbers=[]

for num in numbers:
        # using not in operator 
        # not in checks if a value is not present in a variable or list 
     if num not in unique_numbers:
            unique_numbers.append(num)

# the result of the unique number list 

for num in unique_numbers:
    print(num, end=" ")




