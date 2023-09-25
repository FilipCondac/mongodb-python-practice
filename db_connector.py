
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        uri = os.getenv("MONGO_URI")
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client["simply-pet"]
        return db
    except Exception as e:
        print(e)
        return None
        
def get_pets():
    try:
        db = get_connection()
        mycol = db["pets"]
        pets = list(mycol.find())
        return pets
    except Exception as e:
        print(e)
        return None