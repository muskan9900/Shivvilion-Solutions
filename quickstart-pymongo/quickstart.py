from pymongo import MongoClient

uri = ""
client = MongoClient(uri)

try:
    database = client.get_database("test")
    first = database.get_collection("first")

    # Query 
    query = { "name": 'mike' }
    first = first.find_one(query)

    print(first)

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
