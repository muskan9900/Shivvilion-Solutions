""" deleing operations """

import pymongo

myclient=pymongo.MongoClient("mongodb+srv://user_1:1WAj2yu5TWxdvGpr@test1.xumyeeu.mongodb.net/")
mydb=myclient["test"]
mycol=mydb["first"]

# myquery={"address": 'valley 652'}

# mycol.delete_one(myquery)

# to delete many documenst use $regex and delete_many

# myquery={"address": {"$regex" : "^v"}}

# x=mycol.delete_many(myquery)

# print(x.deleted_count, "documents deleted ")

# to delete all documents without any condition or specific feild 

x=mycol.delete_many({})
print(x.deleted_count, "documents deleted ")

