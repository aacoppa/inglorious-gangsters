from pymongo import MongoClient

client = MongoClient()
db = client.college

def checkDB():
    if len(db.colleges.find()) == 0:
        return False
    else:
        return True

def db_store_college(College):
    db.colleges.insert({'name':College.name, 'location':College.location,
                        'rank':College.rank, 'sats':College.sats,
                        'size':College.size, 'tuition':College.tuition,
                        'address':College.address, 'state':College.state})

def db_college_exits(College_name):
    College = db.colleges.find({'name':College_name})
    if len(College) == 0:
        return False
    return True
