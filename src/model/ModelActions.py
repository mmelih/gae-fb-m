'''
Created on Oct 19, 2010

@author: cagatay.yuksel
'''

from Models import *

def getFbUser(self, cookie):
    return User.get_by_key_name(cookie["uid"])

def saveUser(profile,cookie):
    user = User(key_name=str(profile["id"]),
                                id=str(profile["id"]),
                                name=profile["name"],
                                profile_url=profile["link"],
                                access_token=cookie["access_token"])
    user.put()
    return user