from pymongo import MongoClient

client = MongoClient()
db = client.college

def checkDB():
    if len(db.colleges.find()) == 0:
        return False
    else:
        return True

def initDB():
    """
    init db from various sources
    """
