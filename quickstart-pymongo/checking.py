""" creating and checking the existing database """

import pymongo

#  my client holds the connection
# myclient=pymongo.MongoClient("")
#  my db holds the connection 
# mydb= myclient["test"] # existing data base just to check the program

# # check if database exist
# print(myclient.list_database_names())

# # check if a specific database by name

# dblist=myclient.list_database_names()
# if "test" in dblist:
#     print("the database exists")

# similar way to check for collection
myclient=pymongo.MongoClient("")

mydb= myclient["test"] # existing data base just to check the program

#  variable for collection(tables)
# my col holds my db with specified collection
mycol=mydb["first"]
# check if database exist
print(mydb.list_collection_names())

# check if a specific database by name

col_list=mydb.list_collection_names()
if "first" in col_list:
    print("the collection exists")








""" insert command  """
