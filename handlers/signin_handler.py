from handlers.base_handler import BaseHandler
from modules.auth import check_password
from models.user import User


class SignInHandler(BaseHandler):
    def get(self):
        args = {
            'hide_navigation': True,
            'error_message': self.request.get('error')
        }

        self.render('signin.html', **args)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        users = User.all().filter('username =', username).fetch(1)
        if len(users) == 0:
            self.response.set_status(401)
            self.redirect('/login?error=Could not find such username')
            return

        user = users[0]

        if check_password(password, user.password):
            self.save_auth_cookie(user.key().id())
            self.redirect('/')
        else:
            self.response.set_status(401)
            self.redirect('/login?error=The passwords did not match')
