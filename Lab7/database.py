from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseConnection:
    def __init__(self):
        client = MongoClient(port=int(os.getenv('PORT')), username=os.getenv('USERNAME'),
                             password=os.getenv("PASSWORD"))
        self.db = client.application

    def get_all_data(self):
        return self.db.users.find({}, {"_id": 0})
