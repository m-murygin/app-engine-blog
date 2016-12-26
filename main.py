import webapp2

from handlers.index_handler import IndexHandler
from handlers.new_post_handler import NewPostHandler
from handlers.post_handler import PostHandler


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/newpost', NewPostHandler),
    ('/post/(\d+)', PostHandler),
], debug=True)
