from pymongo import MongoClient
client = MongoClient()
db = client.college

def db_add_user(uid, name, email, pw):
    db.user.insert({'uid':uid, 'pw':pw, 
                    'name':name, 'email':email})

def get_next_uid():
    try:
        return max([user['uid'] for user in db.user.find()]) + 1
    except ValueError:
        return 1

def db_valid_upass(email,pw):
    user = db.user.find_one({'email': email})
    if not user:
        return False
    if user['pw'] == pw:
        return True
    return False

def db_name_taken(name):
    user = db.user.find_one({'name':name})
    if not user:
        return False
    return True

def db_email_taken(email):
    return not db.user.find_one({'email':email}) == None
    

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
