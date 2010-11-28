'''
Created on Oct 19, 2010

@author: cagatay.yuksel
'''
from gaeisha.PageHandler import PageHandler
from model.ModelActions import getByTitle

class ShowHandler(PageHandler):
    TEMPLATE_FILE = "show.html"
    
    def get(self):
        self.error(404);
        return
    
    def rpcGetTitle(self, title):
        return getByTitle(title)