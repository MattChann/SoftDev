# Team Pineapple: Matthew Chan and Brian Moses
# SoftDev pd2
# K09 -- Yummy Mongo Py
# 2020-02-27

import pymongo
from pymongo import MongoClient
from bson.json_util import loads
from urllib.request import urlopen
import json
from math import cos

client = MongoClient()
db = client.buildings
restaurants = db.restaurants

#=== VARIOUS FIND FUNCTIONS BASED ON DIFFERENT PARAMETERS =======
# Finds all restaurants in a specified borough
def find_borough(borough):
    return [restaurant for restaurant in restaurants.find({"borough": f"{borough}"})]

# Finds all restaurants in a specified zip code
def find_zipcode(zipcode):
    return [restaurant for restaurant in restaurants.find({"address.zipcode": f"{zipcode}"})]

# Finds all restaurants in a specified zip code and with a specified grade
def find_zipcode_and_grade(zipcode, grade):
    return [restaurant for restaurant in restaurants.find({"address.zipcode": f"{zipcode}", "grades.grade": grade})]

# Finds all restaurants in a specified zip code with a score below a specified threshold
def find_zipcode_and_score(zipcode, score_threshold):
    return [restaurant for restaurant in restaurants.find({"address.zipcode": f"{zipcode}", "grades.score": {"$lt": score_threshold}})]

# (Clever Function)
# Finds all restaurants in an approximate 1 mile by 1 mile square around you (using your IP Address location approximation)
def find_near(ip_address=None):
    if ip_address == None:
        ip_data = json.loads(urlopen(f"http://ip-api.com/json/").read())
    else:
        ip_data = json.loads(urlopen(f"http://ip-api.com/json/{ip_address}").read())

    ip_latitude = ip_data["lat"]
    ip_longitude = ip_data["lon"]

    # Each degree of latitude is approximately 69 miles apart
    MILE_IN_LATITUDE = 1 / 69
    # 1° longitude = cosine (latitude) * length of degree (miles) at equator
    MILE_IN_LONGITUDE = 1 / (cos(ip_latitude) * 69)

    lat_lower = ip_latitude - MILE_IN_LATITUDE
    lat_higher = ip_latitude + MILE_IN_LATITUDE
    lon_lower = ip_longitude + MILE_IN_LONGITUDE
    lon_higher = ip_longitude - MILE_IN_LONGITUDE
    # print(f"{lat_lower, lat_higher, lon_lower, lon_higher}")

    return [restaurant for restaurant in restaurants.find({"address.coord.1": {"$lt": lat_higher, "$gt": lat_lower},
                                                           "address.coord.0": {"$lt": lon_higher, "$gt": lon_lower}})]

# print(find_borough(""))
# print(find_borough("Bronx"))

# print(find_zipcode(11225))
# print(find_zipcode(11225))
# print(find_zipcode(10013))

# print(find_zipcode_and_grade(10013, "Z"))
# print(find_zipcode_and_grade(10013, "A"))

# print(find_zipcode_and_score(10013, 0))
# print(find_zipcode_and_score(10013, 25))

print(find_near())
print(find_near('149.89.150.131'))