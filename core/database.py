from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from config.settings import MONGO_URI, DB_NAME, COLLECTION_NAME
from models.schemas import Flight
from core.logger import init_logger


logger = init_logger("database")


client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


try:
    client.admin.command("ping")
except ConnectionFailure:
    logger.error("Server not available")


def insert_data(data: Flight):
    try:
        collection.insert_one(data.model_dump())
    except:
        logger.warning(f"Couldn't insert element: { data.model_dump() }")
    

def update_data(data: Flight):
    try:
        collection.update_one({ "flight_uuid": data.flight_uuid }, { "$set": data.model_dump(exclude= "flight_uuid") })
    except:
        logger.warning(f"Couldn't update element of flight_uuid: { data.flight_uuid }")
    

def get_data_by_uuid(flight_uuid: str):
    try:
        flight = collection.find_one({ "flight_uuid": flight_uuid })
    except:
        logger.warning(f"Couldn't find element of flight_uuid: { flight_uuid }")
    
    if flight:
        return flight