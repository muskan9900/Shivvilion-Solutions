""" droping the collection """

import pymongo

myclient=pymongo.MongoClient("")

mydb=myclient["test"]
mycol=mydb["persons"]

mycol.drop()

print(mydb.list_collection_names())

coll_list=mydb.list_collection_names()

if "persons" in coll_list:
    print("collection persons exits")

else:
    print("collection persons deleted")







