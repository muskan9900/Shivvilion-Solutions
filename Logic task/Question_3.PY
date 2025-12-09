def find_second_largest_unique(numbers):
    # to check the length of the numbers 
    if len(numbers) < 2:
        return None
    
    # iniialize first_max and second_max to negative infinity
    # negative infinity ensures that the number in the data will be greater or equal to its initial values
    
    first_max= second_max=float("-inf")

    for num in numbers:
        if num> first_max:
            second_max= first_max
            first_max=num
        elif first_max> num> second_max:
            second_max=num # to check second_max 

    # Check if a unique second largest number was found
    if second_max == float('-inf') or second_max == first_max:
        return None
    else:
        return second_max

# list to check second_max
list1 = [10, 20, 4, 45, 99, 99, 67]
print(f"The second largest unique number in {list1} is: {find_second_largest_unique(list1)}")



     
    
    