""" insert commnad  """

import pymongo

#  my client holds the connection
myclient=pymongo.MongoClient("mongodb+srv://user_1:1WAj2yu5TWxdvGpr@test1.xumyeeu.mongodb.net/")
#  my db holds the connection 
mydb= myclient["test"] # existing data base just to check the program

# mycol holds mydb
mycol=mydb['first'] 

# creating a document(record) to be inserted 
mydoc={"name": "jhon", "address": "Highway 37"}

# using insert_one() method inserting record to collection
#  insert_one() inserts only one document, one {}
x=mycol.insert_one(mydoc)

#  returning the inserted document through _id field
print(x.inserted_id)

for f in mycol.find():
    print(f)
