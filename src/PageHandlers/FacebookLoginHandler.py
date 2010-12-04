'''
Created on 01 Ara 2010

@author: melih
'''

import urllib
import cgi
import time


from django.utils import simplejson as json
from gaeisha.PageHandler import PageHandler
from model import *
from config import facebookConf
from facebook import facebook

class FacebookLoginHandler(PageHandler):
    TEMPLATE_FILE = "main.html"
    def preprocess(self):     
        verification_code = self.request.get("code")
        args = dict(client_id=facebookConf.FACEBOOK_APP_ID, redirect_uri=self.request.path_url)
        if self.request.get("code"):
            args["client_secret"] = facebookConf.FACEBOOK_APP_SECRET
            args["code"] = self.request.get("code")
            response = cgi.parse_qs(urllib.urlopen(
                "https://graph.facebook.com/oauth/access_token?" +
                urllib.urlencode(args)).read())
            access_token = response["access_token"][-1]

            # Download the user profile and cache a local instance of the
            # basic profile info
            profile = json.load(urllib.urlopen(
                "https://graph.facebook.com/me?" +
                urllib.urlencode(dict(access_token=access_token))))
            
            #TODO: may fail if the user removed app from facebook app list and then login again
            rUser = ModelActions.getFacebookUser(self, str(profile["id"]))

            if(not rUser):
                rUser = ModelActions.registerFacebookUser(self, profile["name"], 
                                                  str(profile["id"]), access_token)
            else:
                ModelActions.updateFacebookUser(self, str(profile["id"]), "facebookAccessToken", access_token)  
                  
            facebook.set_cookie(self.response, "fb_user", str(profile["id"]),
                       expires=time.time() + 30 * 86400)
            self.redirect("/")
        else:
            self.redirect(
                "https://graph.facebook.com/oauth/authorize?" +
                urllib.urlencode(args))
        return
    
    


    