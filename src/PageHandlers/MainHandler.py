'''
Created on Oct 18, 2010

@author: cagatay.yuksel
'''

from gaeisha.PageHandler import PageHandler
from model import *


class MainHandler(PageHandler):
    TEMPLATE_FILE = "main.html"
    def preprocess(self):
        templateDict = dict()
        
        
        user = self.checkFacebookSession()
        
        if(not user):
            self.showLoginForm()
        else:
            templateDict["welcome_message"] = self.user["name"]

        
        self.writeTemplate(self.TEMPLATE_FILE, templateDict)
        return
    
    


    