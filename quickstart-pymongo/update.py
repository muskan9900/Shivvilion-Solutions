""" updating the query  """

import pymongo 

myclient=pymongo.MongoClient("")

mydb=myclient["test"]
mycol=mydb["first"]

# updating one value

# query={"address" : "Mountain 21"}

# new_values={"$set": {"name" : "Minnie"}}

# x=mycol.update_one(query,new_values)

# for x in mycol.find():
#     print(x)

# update many values 

query={"name" : {"$regex": "^.i"}}

new_values={"$set": {"address" : "Highway 37"}}

x=mycol.update_many(query,new_values)

for x in mycol.find():
    print(x)

