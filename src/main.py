from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from PageHandlers.MainHandler import MainHandler
from PageHandlers.FacebookLoginHandler import FacebookLoginHandler
from PageHandlers.GetUsersHandler import GetUsersHandler


application = webapp.WSGIApplication([('/', MainHandler),
                                      ('/facebookLogin',FacebookLoginHandler),
                                      ('/getUsers', GetUsersHandler)
                                      ])

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
