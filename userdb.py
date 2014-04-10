from pymongo import MongoClient

client = MongoClient()
db = client.college

def addUser(list):
    db.user.insert({'id':list['id'], 'pw':list['pw'], 'name':list['name'], 'address':list['address'], 'email':list['email'],
                    'sat1':list['sat1'], 'sat2':list['sat2'], 'phone':list['phone'], 'preferences':list['preferences']})
    
def getPrefs(id):
    return db.user.find_one({'id':id}, fields={'preferences':True, '_id':False})
    
    
def loadUser(id):
    return db.user.find_one({'id':id})

