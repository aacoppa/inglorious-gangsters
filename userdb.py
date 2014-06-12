from pymongo import MongoClient

client = MongoClient()
db = client.college

def db_add_user(uid, name, email, pw):
    db.user.insert({'uid':uid, 'pw':pw, 
                    'name':name, 'email':email})

def get_next_uid():
    return len(db.user.find()) + 1

def db_valid_upass(email,pw):
    user = db.user.find_one({'email',email}, fields{'preferences':True, '_id':False})
    if users['pw'] == pw:
        return True
    return False

def db_name_taken(uid):
    user = db.user.find({'uid':uid})
    return len(user) == 1

def db_email_taken(email):
    return len(db.user.find({'email':email})) == 1
    

def getPrefs(id):
    return db.user.find_one({'id':id}, fields={'preferences':True, '_id':False})    
    
def db_load_user(id):
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
