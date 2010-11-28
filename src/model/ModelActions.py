'''
Created on Oct 19, 2010

@author: cagatay.yuksel
'''

from Models import *

def getByTitle(title):
    t = Entry.all()
    t.filter("title=", title)
    result = t.get()
    return result

def putEntry(title, content): 
    entry = Entry()
    entry.title = title
    entry.content = content
    entry.put()
    return

def downVote(entryKey):
    def txn(key):
        entry = db.get(key)
        entry.rating -= 1
        entry.put()
        return entry.rating
    return db.run_in_transaction(txn, entryKey)

def upVote(entryKey):
    def txn(key):
        entry = db.get(key)
        entry.rating += 1
        entry.put()
        return entry.rating
    return db.run_in_transaction(txn, entryKey)

def ogrenciEkle(isim,numara):
    ogrenci = Ogrenci()
    ogrenci.isim = isim
    ogrenci.numara = int(numara)
    ogrenci.put()
    