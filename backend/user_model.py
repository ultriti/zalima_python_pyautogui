from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']

class User:
    @staticmethod
    def get_all():
        return list(db.users.find())
