from handlers.base_handler import BaseHandler


class NewPostHandler(BaseHandler):
    def get(self):
        self.render('new_post.html')

    def post(self):
        pass
