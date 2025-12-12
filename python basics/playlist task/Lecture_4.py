""" practice question of Lecture 4 Dictionary and sets """
 
""" Dictionary are mutable, unordered data type 
# its key are unique , no duplicate keys 
# has key value pairs 
 """

info = { 

    "key": "xyz",
    "value": "pair",
    "subjects": ["python","dsa","ui/ux"],
    "learning": "dicttionary",
    "age": 35,
    "score": 45.5,
    "is_adult":  True,
     1: "hello"
}
info["welcome"]="hello" # adding a new element 

print(info["is_adult"])


#  creating a empty dict

null_Dict={


}

#  assigning value to null_Dict

null_Dict["name"]="hello"

print(null_Dict)

#  creating a nested dict 

nest_Dict={

        "score": 666,
        "subjects":{

            "key": "value"
        }
}

print(nest_Dict)

# dictionary methods

print((list(nest_Dict.keys())))
# to print the keys in list , casting the way how we cast int, string, float

# to print total numbers of keys of a dict
print(len(nest_Dict)) # len of keys is only printed 
print(len(list(nest_Dict.keys()))) # this is also a way to print 

print(len(nest_Dict.values()))# prints the len of values 
print(nest_Dict.values()) # prints the values of dict
print(list(nest_Dict.values()))  # prints the list of values

print(info.items())
print(nest_Dict.items())

# to select a paticular key-value pair from the given dict

nest_Dict.items()
pairs=list(nest_Dict.items())
print(pairs[0]) 

# to get the value by its key in dict we have following ways

print(nest_Dict["score"]) # generall and simple way to get the value
# also shows error if the key not found
# print(nest_Dict["score1"])


# second way to get value from key is by get () 
print(nest_Dict.get("score"))
#  this shows no error only returns none if the key is not found
print(nest_Dict.get("score_1"))

# updating and key value pair by update() in an existing dict
info.update({"true":"false"})
print(info)

# same key but with different value so the key doesnt not change it over writes the value
info.update({"true":"not true"})
print(info)

""" sets """

# sets are mutable and stores only immutable data types 
# they are unodered items , no duplicates only unique values 
#  {} are used 
#  set elements are immutable 

# creating a set

collection={1,2,3,4,5,6,7,8,"hello","welcome",2,2,2}

print(collection)
print(type(collection))

#  to see how sets are unodered
collection={1,2,3,4,5,6,7,8,"hello","welcome",2,2,2, 9,0,"its python","yyyy","tyty"}
print(collection)

# creating empty set
collection={} # its generates empty dict not set 
print(type(collection))

# right way to create empty set is adding ()

emp_set=set() # even though the set syntax is {} but for creating empty set  it is set()
print(type(emp_set))

# set methods to add elements by add(), remove()
emp_set.add(1)
emp_set.add(2)
emp_set.add(2)
emp_set.add(3)
emp_set.remove(2)
emp_set.remove(3)
emp_set.add("hello")
emp_set.add((1,2,3,4,5,6,7))
# list cannot be added as they are unhasable 
# emp_set.add([1,2,3,4,5,6,7])
emp_set.clear() # empties the set 
print(len(emp_set))
print(emp_set)


# new list to check the pop() , randomly pops the element from the list 

collection={"xyz","try","tyzx","hytr"}

print(collection.pop())
print(collection.pop())
print(collection.pop())
print(collection.pop())
# print(collection.pop())

# important methods in sets 
# set union function

set1={1,2,3}
set2={3,4,5,2}
# combines both set values  and returns new value 
print(set1.union(set2)) # o/p {1,2,3,4,5}
print(set1)
print(set2)

# set intersection  function

set1={1,2,3,4}
set2={4,5,6,4,7}

# combines common values and return new set 

print(set1.intersection(set2)) # o/p {4}
print(set1)
print(set2)

# practice question 1 store the following word meaning  in a python dictionary:

meanings={
    "table": ["a peice of furniure ", "list of facts  and figures"],
     "cat": "a small animal"
}

print(meanings)

""" practice question 2 you are given a list of subjects for students. 
Assume one classroom  is required for 1 subjects , how many classroom are needed by all students 
 """ 

class_Sub={"python","java","c++","JS","C"}

print(len(class_Sub))

""" practice question 3 
 """ 

empty_dict={}

x= int(input("enter your marks: "))
empty_dict.update({"maths": x})
print(empty_dict)


y= int(input("enter your marks: "))
empty_dict.update({"science": y})
print(empty_dict)


z= int(input("enter your marks: "))
empty_dict.update({"english": z})
print(empty_dict)


""" practice question 4
 """ 

# step 1 create a empty set

emp_set= set()

emp_set.add("9")
            
emp_set.add(9.0)

print(emp_set)


















