from .base import BaseHandler


class NewPost(BaseHandler):
    def get(self):
        self.render('new_post.html')

    def post(self):
        pass
