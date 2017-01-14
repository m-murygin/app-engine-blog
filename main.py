import webapp2

from handlers.index_handler import IndexHandler
from handlers.new_post_handler import NewPostHandler
from handlers.post_handler import PostHandler
from handlers.signup_handler import SignUpHandler
from handlers.welcome_haldler import WelcomeHandler
from handlers.signin_handler import SignInHandler
from handlers.logout_handler import LogoutHandler
from handlers.blog_api import BlogApi


app = webapp2.WSGIApplication([
    (r'^/$', IndexHandler),
    (r'^/.json$', BlogApi),
    (r'^/newpost/?$', NewPostHandler),
    (r'^/(\d+)/?$', PostHandler),
    (r'^/signup/?$', SignUpHandler),
    (r'^/login/?$', SignInHandler),
    (r'^/welcome/?$', WelcomeHandler),
    (r'^/logout/?$', LogoutHandler),
], debug=True)
