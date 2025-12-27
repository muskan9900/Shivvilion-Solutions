""" droping the collection """

import pymongo

myclient=pymongo.MongoClient("mongodb+srv://user_1:1WAj2yu5TWxdvGpr@test1.xumyeeu.mongodb.net/")

mydb=myclient["test"]
mycol=mydb["persons"]

mycol.drop()

print(mydb.list_collection_names())

coll_list=mydb.list_collection_names()

if "persons" in coll_list:
    print("collection persons exits")

else:
    print("collection persons deleted")







