""" creating and checking the existing database """

import pymongo

#  my client holds the connection
# myclient=pymongo.MongoClient("mongodb+srv://user_1:1WAj2yu5TWxdvGpr@test1.xumyeeu.mongodb.net/")
#  my db holds the connection 
# mydb= myclient["test"] # existing data base just to check the program

# # check if database exist
# print(myclient.list_database_names())

# # check if a specific database by name

# dblist=myclient.list_database_names()
# if "test" in dblist:
#     print("the database exists")

# similar way to check for collection
myclient=pymongo.MongoClient("mongodb+srv://user_1:1WAj2yu5TWxdvGpr@test1.xumyeeu.mongodb.net/")

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
