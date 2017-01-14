from handlers.base_handler import BaseHandler
from models.post import Post


class BlogApi(BaseHandler):
    def get(self):
        posts = Post.all().order('-created')

        dict_posts = []
        for post in posts:
            dict_posts.append(post.to_json())

        self.send_json(dict_posts)
