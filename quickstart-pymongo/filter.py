
""" filtering the output  """
import pymongo

myclient=pymongo.MongoClient("")

mydb=myclient['test']
mycol=mydb['first']

# this prints the specific document given in the myquery
# myquery={"address":"valley 652"}

# mydoc=mycol.find(myquery)

# for x in mydoc:
#   print(x)


# applying conditions 

# myquery={"address":{"$gt" :"S"}}

# mydoc=mycol.find(myquery)

# for x in mydoc:
#   print(x)


# filtering with regex

myquery={"address":{"$regex" :"^v"}}

mydoc=mycol.find(myquery)

for x in mydoc:
  print(x)

