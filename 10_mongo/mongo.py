# Team pp: Matthew Chan and Justin Chen
# SoftDev pd2
# K10 -- Import/Export Bank
# 2020-03-03

'''
Reddit TodayILearned Subreddit posts and details about those posts
Link: https://www.reddit.com/r/todayilearned.json
Import Mechanism: import as json then take the contents list and use each entry in that as a document in mongodb
'''

import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.pp
reddit = db.reddit

# #=== VARIOUS FIND FUNCTIONS BASED ON DIFFERENT PARAMETERS =======

def find_author(author):
    return list(reddit.find({"data.author": f"{author}"}))

def find_min_upvotes(upvote_threshold):
    return list(reddit.find({"data.ups": {"$gt": upvote_threshold}}))

def find_max_downvotes(downvote_threshold):
    return list(reddit.find({"data.downs": {"$lt": downvote_threshold}}))

def find_min_awards(awards_threshold):
    return list(reddit.find({"data.total_awards_received": {"$gt": awards_threshold}}))

def find_random():
    return list(reddit.aggregate([{"$sample": {"size": 1}}]))[0]


# print(find_author("design-responsibly"))
# print(find_author("asdfg"))

# print(find_min_upvotes(20000))
# print(find_min_upvotes(9999999))

# print(find_max_downvotes(4))
# print(find_max_downvotes(-1))

# print(find_min_awards(0))
# print(find_min_awards(999))

print(find_random())