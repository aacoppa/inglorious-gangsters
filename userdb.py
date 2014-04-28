from pymongo import MongoClient

client = MongoClient()
db = client.college

def addUser(list):
    db.user.insert({'id':list['id'], 'pw':list['pw'], 
                    'info':('name':list['name'], 'address':list['address'], 'email':list['email'], 'phone':list['phone']),
                    'scores':[list['sat1'], list['sat2']), 'preferences':list['preferences']})
    
def getPrefs(id):
    return db.user.find_one({'id':id}, fields={'preferences':True, '_id':False})    
    
def loadUser(id):
    return db.user.find_one({'id':id})

def getScores(id):
    return db.user.find_one({'id':id}, fields={'_id':False, 'scores':True})

def getInfo(id):
    return db.user.find_one({'id':id}, fields={'_id':False, 'info':True})

def updateInfo(id, info):
    db.user.update({'id':id}, {'info':info})

def updatePref(id, pref):
    db.user.update({'id':id}, {'info':info})

def updateAddr(id,addr):
    info = getInfo(id)
    info['address'] = addr
    updateInfo(id, info)

def updateEmail(id, email):
    info = getInfo(id)
    info['email'] = email
    updateInfo(id, info)

def updatePhone(id, phone):
    info = getInfo(id)
    info['phone'] = phone
    updateInfo(id, info)
