# users.py
from pymongo import MongoClient

class UserDB:
    def __init__(self, db_url):
        self.client = MongoClient(db_url)
        self.db = self.client["AnimeLordDB"]
        self.collection = self.db["users"]
        
    def add_user(self, user_id, username):
        self.collection.insert_one({"user_id": user_id, "username": username})
    
    def get_user(self, user_id):
        return self.collection.find_one({"user_id": user_id})
      
