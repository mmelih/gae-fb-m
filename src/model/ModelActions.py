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

def getFacebookUser(facebookId):
    registeredUsers = db.GqlQuery("SELECT * FROM User WHERE registirationType = :1 AND facebookId = :2", "facebook", facebookId)
    rUser = registeredUsers.get()
    return rUser

#TODO:
def getAllUsers():
    users = User.all();
    userList = []
    for user in users:
        userList.append([user.name, user.latestLocation.lat, 
                         user.latestLocation.lon])
        
    return userList

def updateFacebookUser(self, facebookId, property, value):
    user = getFacebookUser(self, facebookId)
    property = getattr(user, property)
    user.property = value
    user.put();
    return 

def updateFacebookUserLocation(facebookId, lat, lon):
    user = getFacebookUser(facebookId)
    user.latestLocation = db.GeoPt(lat, lon)
    user.put()
    return
    