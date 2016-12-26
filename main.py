import webapp2

from handlers.index import IndexHandler

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
], debug=True)
