'''
Created on Oct 19, 2010

@author: cagatay.yuksel
'''

from gaeisha.PageHandler import PageHandler
from model.ModelActions import upVote, downVote, putEntry

class PostHandler(PageHandler):
    def get(self):
        self.error(404)
        
        return
    
    def rpcPostEntry(self, title, content):
        putEntry(title, content)
        
        return (title, content)
   
    def rpcUpVote(self, entryKey):
        return upVote(entryKey)
    
    def rpcDownVote(self, entryKey):
        return downVote(entryKey) 