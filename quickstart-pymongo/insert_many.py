""" insert commnad  """

import pymongo

#  my client holds the connection
myclient=pymongo.MongoClient("")
#  my db holds the connection 
mydb= myclient["test"] # existing data base just to check the program

# mycol holds mydb
mycol=mydb['first'] 

# creating a document(record) to be inserted 
#  this multiple documents 
# so using list or consider array 
mydoc=[{"name": "Amy", "address":"Apple st 652"},
       {"name": "Luna", "address":"Mountain 21"},
       {"name": "Hannah", "address":"valley 652"},
       {"name": "William", "address":"central st 954"}]

# using insert_one() method inserting record to collection
#  insert_one() inserts only one document, one {}
x=mycol.insert_many(mydoc)

#  returning the inserted document through _id field
print(x.inserted_ids)

for f in mycol.find():
    print(f)
