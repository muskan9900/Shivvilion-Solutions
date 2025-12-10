# started at 6:30am to 9:00am

"""Write a Python program to check whether a string has balanced parentheses.
 Example:
"(()())" → Balanced
"((())" → Not Balanced
"""

def is_balanced(string):
    # this function removes matching pairs until no pair of brackets if found
    
    # loop for checking balanced and unbalanced
    while "()" in string or "{}" in string or"[]" in string:

        string=string.replace("()","")
        string=string.replace("{}","")
        string=string.replace("[]","")

    # if the string is found empty all the given brackets are matched
        return string ==""
    
    # outputs to check
print(is_balanced("()"))
print(is_balanced("{}"))
print(is_balanced("[]"))





