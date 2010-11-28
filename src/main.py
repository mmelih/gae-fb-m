from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from PageHandlers.MainHandler import MainHandler
from PageHandlers.ShowHandler import ShowHandler
from PageHandlers.PostHandler import PostHandler
from PageHandlers.MelihHandler import MelihHandler


application = webapp.WSGIApplication([('/', MainHandler),
                                      ('/show', ShowHandler),
                                      ('/post', PostHandler),
                                      ('/melih', MelihHandler)
                                      ])

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
