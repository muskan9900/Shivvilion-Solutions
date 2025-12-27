""" limit query  """

import pymongo 

myclient=pymongo.MongoClient("mongodb+srv://user_1:1WAj2yu5TWxdvGpr@test1.xumyeeu.mongodb.net/")

mydb=myclient["test"]
mycol=mydb["first"]

# limit query limits the result 

my_result=mycol.find().limit(2)

for x in my_result:
    print(x)