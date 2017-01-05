from handlers.base_handler import BaseHandler
from modules.auth import USER_COOKIE


class LogoutHandler(BaseHandler):
    def post(self):
        self.response.delete_cookie(USER_COOKIE)
        self.response.set_status(200)
