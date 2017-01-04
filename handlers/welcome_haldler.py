from handlers.base_handler import BaseHandler


class WelcomeHandler(BaseHandler):
    def get(self):
        self.render('welcome.html')
