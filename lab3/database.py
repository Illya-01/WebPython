from pymongo import MongoClient


conn = MongoClient("localhost", 27017)
db = conn["camp"]
campgrounds_db = db["campgrounds"]
users_db = db["users"]
