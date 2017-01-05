from handlers.base_handler import BaseHandler
from modules.verificator import Verificator
from modules.auth import create_user


class SignUpHandler(BaseHandler):
    def get(self):
        self.render('signup.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify_pass = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username=username, email=email)
        hasErrors = False
        if not Verificator.verify_name(username):
            hasErrors = True
            params['name_error'] = Verificator.FAIL_USER_NAME_MES

        if Verificator.verify_equality_passwords(password, verify_pass):
            if not Verificator.verify_password(password):
                hasErrors = True
                params['pass_error'] = Verificator.FAIL_PASS_MESSAGE
            if not Verificator.verify_password(verify_pass):
                hasErrors = True
                params['verify_error'] = Verificator.FAIL_PASS_MESSAGE
        else:
            hasErrors = True
            params['verify_error'] = Verificator.NOT_EQUAL_PASS_MES

        if not Verificator.verify_email(email):
            hasErrors = True
            params['email_error'] = Verificator.FAIL_EMAIL_MES

        if hasErrors:
            self.render('signup.html', **params)
        else:
            user_id = create_user(username, password, email)
            self.save_auth_cookie(user_id)
            self.redirect('/welcome')
