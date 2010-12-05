'''
Created on Oct 18, 2010

@author: cagatay.yuksel
'''

from gaeisha.PageHandler import PageHandler
from model import ModelActions
from django.utils import simplejson

class GetUsersHandler(PageHandler):
    TEMPLATE_FILE = "getUsers.html"
    def preprocess(self):
        templateDict = dict()
        
        user = self.checkFacebookSession()
        
        ModelActions.updateFacebookUserLocation(user.facebookId, 
                                                self.request.get("lat"), self.request.get("lon"))
        users = ModelActions.getAllUsers()
        args = simplejson.dumps(users)
        
        templateDict["content"] = args
        self.writeTemplate(self.TEMPLATE_FILE, templateDict)
        return
    
    


    