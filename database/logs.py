# logs.py
from pymongo import MongoClient

class LogsDB:
    def __init__(self, db_url):
        self.client = MongoClient(db_url)
        self.db = self.client["AnimeLordDB"]
        self.collection = self.db["logs"]
    
    def add_log(self, log_message):
        self.collection.insert_one({"log": log_message})
    
    def get_logs(self):
        return list(self.collection.find())
      
