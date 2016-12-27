from handlers.base_handler import BaseHandler
from models.post import Post


class PostHandler(BaseHandler):
    def get(self, post_id):
        post_id = int(post_id)
        post = Post.get_by_id(post_id)

        if post:
            self.render('post.html', post=post)
        else:
            self.error(404)
