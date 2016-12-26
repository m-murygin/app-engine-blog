from handlers.base_handler import BaseHandler


class PostHandler(BaseHandler):
    def get(self):
        self.render('post.html')
