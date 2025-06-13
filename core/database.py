from pymongo import MongoClient
from config.settings import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def insert_data(data):
    collection = db[COLLECTION_NAME]
    collection.insert_many(data)