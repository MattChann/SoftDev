# Matthew Chan and Brian Moses
# SoftDev pd2
# K09 -- Yummy Mongo Py
# 2020-02-27

import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.buildings
restaurants = db.restaurants

file = open("primer-dataset.json", 'r')
documents = file.readlines()
documents = list(map(lambda doc: eval(doc.strip().replace('$', '').replace('null', 'None')), documents))
file.close()

# print(documents)

result = restaurants.insert_many(documents)

def find_borough(borough):
	pass

def find_zip_code(zip_code):
	pass

def find_zip_and_grade(zip_code, grade):
	pass

def find_zip_and_score(zip_code, score_threshold):
	pass

def clever_find():
	pass
