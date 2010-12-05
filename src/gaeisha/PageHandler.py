'''
Created on Oct 18, 2010

@author: cagatay.yuksel
'''
from facebook import facebook
from config import facebookConf
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from django.utils import simplejson
import os.path
from model import ModelActions


class PageHandler(webapp.RequestHandler):
    TEMPLATE_PATH = "../PageTemplates/"

    
    def get(self, templateDict=None):     
        self.preprocess()
        if not templateDict:
            templateDict = dict()      
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
    
    def checkFacebookSession(self):
        rUser = None
        
        user_id = facebook.parse_cookie(self.request.cookies.get("fb_user"))
        if user_id:
            #Check if we already registered the user
            rUser = ModelActions.getFacebookUser(user_id)

        return rUser

    
    def showLoginForm(self):
        templateDict = dict()
        templateDict["login_error"] = "no connect session"
        self.writeTemplate(self.TEMPLATE_FILE, templateDict)
        return

    def writeTemplate(self, templateFile, templateDict):
        templatePath = os.path.join(os.path.dirname(__file__), self.TEMPLATE_PATH + templateFile)
        self.response.out.write(template.render(templatePath, templateDict))    
        return
    
    def writeJson(self, data):
        self.response.out.write(simplejson.dumps(data))
        return
    