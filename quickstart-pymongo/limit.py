""" limit query  """

import pymongo 

myclient=pymongo.MongoClient("")

mydb=myclient["test"]
mycol=mydb["first"]

# limit query limits the result 

my_result=mycol.find().limit(2)

for x in my_result:
    print(x)