# Matthew Chan and Brian Moses
# SoftDev pd2
# K09 -- Yummy Mongo Py
# 2020-02-27

import pymongo
from pymongo import MongoClient
from bson.json_util import loads

client = MongoClient()
db = client.buildings
restaurants = db.restaurants

file = open("primer-dataset.json", 'r')
documents = file.readlines()
documents = list(map(lambda doc: loads(doc.strip()), documents))
file.close()

# print(documents)

result = restaurants.insert_many(documents)

def find_borough(borough):
	return [restaurant for restaurant in restaurants.find({"borough": f"{borough}"})]

def find_zipcode(zipcode):
	return [restaurant for restaurant in restaurants.find({"zipcode": f"{zipcode}"})]

def find_zipcode_and_grade(zipcode, grade):
	pass

def find_zipcode_and_score(zipcode, score_threshold):
	pass

def clever_find():
	pass
