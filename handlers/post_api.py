from handlers.base_handler import BaseHandler
from models.post import Post


class PostApi(BaseHandler):
    def get(self, post_id):
        post_id = int(post_id)
        post = Post.get_by_id(post_id)

        if post:
            self.send_json(post.to_json())
        else:
            self.error(404)
