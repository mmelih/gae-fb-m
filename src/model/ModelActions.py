'''
Created on Oct 19, 2010

@author: cagatay.yuksel
'''

from Models import *



def registerUser(self, newName, newRegistirationType = "normal"):
    user = User(name = newName, registirationType = newRegistirationType)
    user.put()
    return user

def registerFacebookUser(self, name, facebookId, facebookAccessToken):
    user = registerUser(self, name,"facebook")
    user.facebookId = facebookId
    user.facebookAccessToken = facebookAccessToken
    user.put()
    return user

def getFacebookUser(self, facebookId):
    registeredUsers = db.GqlQuery("SELECT * FROM User WHERE registirationType = :1 AND facebookId = :2", "facebook", facebookId)
    rUser = registeredUsers.get()
    return rUser

def updateFacebookUser(self, facebookId, property, value):
    result = db.GqlQuery("UPDATE User SET :1 = :2 WHERE facebookId = :3", property, value,  facebookId)
    return 
    