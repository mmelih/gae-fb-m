'''
Created on Aug 20, 2010
 
@author: cagatay.yuksel
'''

from google.appengine.ext import db

  
    
class User(db.Expando):
    name = db.StringProperty(required=True)
    registirationType = db.StringProperty(required=True, 
                                          choices=set(["normal","facebook", "google"]))
    latestLocation = db.GeoPtProperty()

