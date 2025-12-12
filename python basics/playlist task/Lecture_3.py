"""practice question of lecture 3 LIST AND TUPLES
"""

# Question 1 WAP to ask the user to enter names of their 3 favourite movies  and store them in a list 

movie_1=input("enter the movie name 1: ")

movie_2=input("enter the movie name 2: ")

movie_3=input("enter the movie name 3: ")

movie_list=[]

""" 
# another way to answer this question to directly put the variables into list
movie_list=[movie_1,movie_2,movie_3]
"""

movie_list.append(movie_1)
movie_list.append(movie_2)
movie_list.append(movie_3)

print(movie_list)

# Question 2 WAP to check if a list contains a palindrome  of elements (using a copy method)

list_1=[1,2,1]
list_2=[1,2,3]


list1_copy=list_1.copy() # makes a shallow copy
list1_copy.reverse()
list2_copy=list_2.copy()
list2_copy.reverse()


if(list_2==list2_copy):
    print("palindrome")

else:
    print("not a palindrome ")


# Question 3 WAP to count  the number  of students with the "A" grade in the following tuple 

tup=("c","D","A","B","B","A")

print(tup.count("A"))

# Question 4 WAP to sort a list  from Ascending to descending

List=["c","D","A","B","B","A"]
List.sort()
print(List)







































