import webapp2

from handlers.index_handler import IndexHandler
from handlers.new_post_handler import NewPostHandler
from handlers.post_handler import PostHandler
from handlers.signup_handler import SignUpHandler
from handlers.welcome_haldler import WelcomeHandler
from handlers.signin_handler import SignInHandler

app = webapp2.WSGIApplication([
    (r'/', IndexHandler),
    (r'/newpost', NewPostHandler),
    (r'/(\d+)', PostHandler),
    (r'/signup', SignUpHandler),
    (r'/login', SignInHandler),
    (r'/welcome', WelcomeHandler),
], debug=True)
