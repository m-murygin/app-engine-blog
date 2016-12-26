import webapp2

from handlers.index import IndexHandler
from handlers.new_post import NewPost


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/newpost', NewPost),
], debug=True)
