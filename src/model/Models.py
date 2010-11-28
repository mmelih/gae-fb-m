'''
Created on Aug 20, 2010
 
@author: cagatay.yuksel
'''

from google.appengine.ext import db

class Entry(db.Model):
    title = db.StringProperty()
    author = db.UserProperty(auto_current_user_add = True)
    content = db.TextProperty()
    rating = db.IntegerProperty(default=0)
    
    dateAdded = db.DateTimeProperty(required=True, auto_now_add=True)
    
class Ogrenci(db.Model):
    isim = db.StringProperty()
    numara = db.IntegerProperty(default = 0)
