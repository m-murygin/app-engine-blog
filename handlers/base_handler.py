import os
import webapp2
import jinja2
import logging

from modules.auth import USER_COOKIE, get_user_from_token, generate_auth_token

template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        auth_token = self.request.cookies.get(USER_COOKIE)
        if auth_token:
            kw['user'] = get_user_from_token(auth_token)

        self.response.out.write(render_str(template, **kw))

    def handle_exception(self, exception, debug):
        # Log the error.
        logging.exception(exception)

        # Set a custom message.
        self.response.write('An error occurred.')

        # If the exception is a HTTPException, use its error code.
        # Otherwise use a generic 500 error code.
        if isinstance(exception, webapp2.HTTPException):
            self.response.set_status(exception.code)
        else:
            self.response.set_status(500)

    def save_auth_cookie(self, user_id):
        secure_id = generate_auth_token(user_id)
        self.response.set_cookie(USER_COOKIE, secure_id)


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)
