""" sort query  """

import pymongo

myclient=pymongo.MongoClient("mongodb+srv://user_1:1WAj2yu5TWxdvGpr@test1.xumyeeu.mongodb.net/")

mydb=myclient["test"]
mycol=mydb["first"]

mydoc=mycol.find().sort("name",1)

for x in mydoc:
    print(x)

# sorting in descending use {"name",-1}