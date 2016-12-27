from handlers.base_handler import BaseHandler
from models.post import Post


class NewPostHandler(BaseHandler):
    def get(self):
        self.render('new_post.html')

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            post = Post(subject=subject, content=content)
            post.put()

            post_id = str(post.key().id())
            self.redirect('/%s' % post_id)
        else:
            error = 'You should write both subject and content.'
            self.render_form(subject, content, error)
