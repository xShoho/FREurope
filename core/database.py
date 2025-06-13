from pymongo import MongoClient

from config.settings import MONGO_URI, DB_NAME, COLLECTION_NAME
from models.schemas import Flight


client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


def insert_data(data: Flight):
    collection.insert_one(data.model_dump())
    

def update_data(data: Flight):
    collection.update_one({ "flight_uuid": data.flight_uuid }, { "$set": data.model_dump(exclude= "flight_uuid") })
    

def get_data_uuid(flight_uuid: str):
    flight = collection.find_one({ "flight_uuid": flight_uuid })
    
    if flight:
        return flight