'''
Created on Oct 19, 2010

@author: cagatay.yuksel
'''

from Models import *



def registerUser(self, name, registirationType = "normal"):
    user = User()
    user.name = name
    user.registirationType = registirationType
    user.put()
    return user

def registerFacebookUser(self, name, facebookId, facebookAccessToken):
    user = registerUser(name,"facebook")
    user.facebookId = facebookId
    user.facebookAccessToken = facebookAccessToken
    return user

def getFacebookUser(self, facebookId):
    registeredUsers = db.GqlQuery("SELECT * FROM User WHERE registirationType =: 1 AND facebookId = :2", "facebook", facebookId)
    rUser = registeredUsers.get()
    return rUser