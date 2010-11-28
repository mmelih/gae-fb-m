
from gaeisha.PageHandler import PageHandler
from model import *


class MelihHandler(PageHandler):
    TEMPLATE_FILE = "melih.html"
    def preprocess(self):
        ModelActions.ogrenciEkle(self.request.get("isim"), self.request.get("numara"));
        return