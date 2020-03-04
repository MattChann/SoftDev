# Team pp: Matthew Chan and Justin Chen
# SoftDev pd2
# K10 -- Import/Export Bank
# 2020-03-03

import pymongo
from pymongo import MongoClient
import json

#=== POPULATING THE DATABASE =======
client = MongoClient()
db = client.pp
reddit = db.reddit

file = open("todayilearned.json", 'r')
data = json.loads(file.read())
file.close()

# print(documents)
result = reddit.insert_many(data)