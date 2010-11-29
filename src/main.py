from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from PageHandlers.MainHandler import MainHandler



application = webapp.WSGIApplication([('/', MainHandler)
                                      ])

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
