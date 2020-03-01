# Team Pineapple: Matthew Chan and Brian Moses
# SoftDev pd2
# K09 -- Yummy Mongo Py
# 2020-02-27

import pymongo
from pymongo import MongoClient
from bson.json_util import loads

#=== POPULATING THE DATABASE =======
client = MongoClient()
db = client.buildings
restaurants = db.restaurants

file = open("primer-dataset.json", 'r')
documents = file.readlines()
documents = list(map(lambda doc: loads(doc.strip()), documents))
file.close()

# print(documents)
result = restaurants.insert_many(documents)