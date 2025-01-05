import json
from pymongo import MongoClient
from psw import connection_string

# connect
client = MongoClient(connection_string)
database = client["formula-1"]

collection = database["championships"]

# load from file
data = json.load(open("json/dataset.json"))

# upload to MongoDB
collection.insert_many(data)
