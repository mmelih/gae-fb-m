'''
Created on Oct 18, 2010

@author: cagatay.yuksel
'''

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from django.utils import simplejson
import os.path

class PageHandler(webapp.RequestHandler):
    TEMPLATE_PATH = "../PageTemplates/"

    
    def get(self, templateDict=None):
        self.preprocess()
        if not templateDict:
            templateDict = dict()
        
        userLink = self.getUserLink()
        templateDict["usertext"] = userLink[0]
        templateDict["userlink"] = userLink[1]
        
        nick = self.getUserNick()
        templateDict['nick'] = nick
        
        self.writeTemplate(self.TEMPLATE_FILE, templateDict)
        
        return
    
    def post(self):
        args = simplejson.loads(self.request.body)
        func, args = args[0], args[1:]

        if func.startswith("rpc"):
            func = getattr(self, func)
            result = func(*args)
            self.writeJson(result)
        else:
            self.error(404)
        return
    
    def getUser(self):
        return users.get_current_user()
    
    def getUserNick(self):
        nickname = ''
        
        user = self.getUser()
        if user:
            nickname = user.nickname().split('@')[0]
        else:
            nickname = None
        
        return nickname
    
    def getUserLink(self):
        user = self.getUser()
        retVal = ()
        
        if user:
            retVal = ('logout', users.create_logout_url(self.request.uri))
        else:
            retVal = ('login', users.create_login_url(self.request.uri))
        
        return retVal
    
    def writeTemplate(self, templateFile, templateDict):
        templatePath = os.path.join(os.path.dirname(__file__), self.TEMPLATE_PATH + templateFile)
        self.response.out.write(template.render(templatePath, templateDict))
        
        return
    
    def writeJson(self, data):
        self.response.out.write(simplejson.dumps(data))
        return
    