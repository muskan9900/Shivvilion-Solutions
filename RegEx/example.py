""" using regex """
# python has a built in package callled re

# importing regex module

import re

txt="the rain in spain"
x= re.search("^the.*spain$",txt)
print("the search is:",x)

# '^'  this means starting with 'The'
# '*' zero or more occurrences
# '$' ends with 

# methods in regex
# serach()
# findall()
# split()
# sub()
# using meta characters 

# [] a set of characters
# eg [a-m]

txt="the rain in spain"
x= re.findall("[a-m]",txt)
print("the [] result is:",x)

# using '\' signals a special sequence 
# eg "\d"

txt="the rain in  67 spain"
# finds the digit characters
x= re.findall("\d",txt)
print("the \d result is:",x)

#  using '.' 
txt ="hello planet"

#Search for a sequence that starts with "he", 
# followed by two (any) characters, and an "o":

x=re.findall("he..o",txt)
print("the result of '.' is:",x)

# using '*'
# it means zero or more occurences

txt="hello planet"

#Search for a sequence that starts with "he", 
# followed by 0 or more 
#  (any) characters, and an "o", where o is the end:
x=re.findall("he.*o",txt)
print("the result of '*':",x)

# using '+'
# it means one or more occurences
#Search for a sequence that starts with "he", 
# followed by 1 or more 
#  (any) characters, and an "o", where o is the end:

x=re.findall("he.+o",txt)
print("the result of '+':",x)

# using '?'
# it means zero or one occurences

#Search for a sequence that starts with "he", 
# followed by 0 or 1
#  (any) characters, and an "o", where o is the end:

x=re.findall("he.?o",txt)
print("the result of '?':",x)

#This time we got no match, because there were not zero, not one,
#  but two characters between "he" and the "o"

# using {} 
# Exactly the specified number of occurrences
# "he.{2}o"

x=re.findall("he.{2}o",txt)
print("the result of {2}:",x)


# '|' 
txt="the rain in spain falls mainly in the plain"
#Check if the string contains either "falls" or "stays":

x=re.findall("falls|stays",txt)
print("the result of |is:",x)

if x:
    print("yes, there is at leat one match!")

else:
    print("No,match!")

# using split() function
# here "\s" special sequence is used , 
# it split the match when white space is found 

txt="the  rain   in   Spain"
x=re.split("\s",txt)
print("the split() result using '\s'",x)

# using sub() which replaces the match with with a string

x=re.sub("\s","9",txt)
print("the sub() result using'\s'is:",x)

# Search for the first white-space character in the string:
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# replaces the first 2 occurrence
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# split the string only at first occurence
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)