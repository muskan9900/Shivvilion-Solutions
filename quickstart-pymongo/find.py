""" viewing through find query """

import pymongo

myclient=pymongo.MongoClient("")

mydb=myclient['test']
mycol=mydb['first']

# the find_one() query returns the first occurrence 
# x=mycol.find_one()

# print(x)

# to find many and print each document 
# using for  loop

# for x in mycol.find():
#     print(x)

# this only finds and returns some feild like name and add  
for x in mycol.find({},{"_id":0,"name":1,"address":1}):
    print(x)

