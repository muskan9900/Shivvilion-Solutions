def to_check_palindrome(str):

 left = 0

 right= len(str) - 1

 while left< right:

    # to check if the characters are at correct position and not same or equal 
    if str[left] != str[right]:
        print("not equal")
        
    # navigating from left to right
    left +=1
    right-=1
    #after navigation if 1 palindrome is found then return 1
    return 1

# to check the given string is palindrome or not call the function 

str="hello"
print(to_check_palindrome(str))



