""" sort query  """

import pymongo

myclient=pymongo.MongoClient("")

mydb=myclient["test"]
mycol=mydb["first"]

mydoc=mycol.find().sort("name",1)

for x in mydoc:
    print(x)

# sorting in descending use {"name",-1}