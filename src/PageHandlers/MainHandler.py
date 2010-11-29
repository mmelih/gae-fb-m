'''
Created on Oct 18, 2010

@author: cagatay.yuksel
'''

from gaeisha.PageHandler import PageHandler
from facebook import facebook
from model import *
from config import facebookConf


class MainHandler(PageHandler):
    TEMPLATE_FILE = "main.html"
    def preprocess(self):
        templateDict = dict()
        
        
        self.facebookapi = facebook.Facebook(facebookConf.FACEBOOK_APP_KEY, facebookConf.FACEBOOK_APP_SECRET)
        
        if not self.facebookapi.check_connect_session(self.request):
            templateDict["login_error"] = "no connect session"
            templateDict["apikey"] = facebookConf.FACEBOOK_APP_KEY
            
        else:
            try:
                self.user = self.facebookapi.users.getInfo(
                                                            [self.facebookapi.uid],
                                                            ['uid', 'name', 'birthday', 'relationship_status'])[0]
                templateDict["welcome_message"] = self.user["name"]
            except facebook.FacebookError:
                templateDict["login_error"] = "no connect session"
                templateDict["apikey"] = facebookConf.FACEBOOK_APP_KEY
                


            
        
        
        
        
        self.writeTemplate(self.TEMPLATE_FILE, templateDict)
        return
    
    


    