# Matthew Chan and Brian Moses
# SoftDev pd2
# K09 -- Yummy Mongo Py
# 2020-02-27

import pymongo
from pymongo import MongoClient
from bson.json_util import loads
import socket
from urllib.request import urlopen
import json
from math import cos

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



#=== VARIOUS FIND FUNCTIONS BASED ON DIFFERENT PARAMETERS =======
# Finds all restaurants in a specified borough
def find_borough(borough):
    return [restaurant for restaurant in restaurants.find({"borough": f"{borough}"})]

# Finds all restaurants in a specified zip code
def find_zipcode(zipcode):
    return [restaurant for restaurant in restaurants.find({"zipcode": f"{zipcode}"})]

# Finds all restaurants in a specified zip code and with a specified grade
def find_zipcode_and_grade(zipcode, grade):
    return [restaurant for restaurant in restaurants.find({"zipcode": f"{zipcode}", "grades.grade": grade})]

# Finds all restaurants in a specified zip code with a score below a specified threshold
def find_zipcode_and_score(zipcode, score_threshold):
    return [restaurant for restaurant in restaurants.find({"zipcode": f"{zipcode}", "grades.score": {$lt: score_threshold}})]

# (Clever Function)
# Finds all restaurants in an approximate 1 mile by 1 mile square around you (using your IP Address location approximation)
def find_near():
    ip_address = socket.gethostbyname(socket.gethostname())
    ip_data = json.loads(urlopen(f"http://ip-api.com/json/{ip_address}").read())

    ip_latitude = ip_data["lat"]
    ip_longitude = ip_data["lon"]

    # Each degree of latitude is approximately 69 miles apart
    MILE_IN_LATITUDE = 1 / 69
    # 1° longitude = cosine (latitude) * length of degree (miles) at equator
    MILE_IN_LONGITUDE = 1 / (cos(ip_latitude) * 69)

    return [restaurant for restaurant in restaurants.find({
        "coord[1]": 
            {$lt: 
                {$add: [ip_latitude, MILE_IN_LATITUDE]}, 
            $gt 
                {$subtract: [ip_latitude, MILE_IN_LATITUDE]}
            }, 
        "coord[0]": 
            {$lt: 
                {$add: [ip_longitude, MILE_IN_LONGITUDE]}, 
            $gt 
                {$subtract: [ip_longitude, MILE_IN_LONGITUDE]}
            }
    })]

# return find_near()