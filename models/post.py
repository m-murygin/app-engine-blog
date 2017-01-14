from google.appengine.ext import db


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    def to_json(self):
        json_obj = db.to_dict(self)
        json_obj['created'] = json_obj['created'].strftime('%c')

        return json_obj
