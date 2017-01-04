import hmac
import random
import string

from models.user import User


SECRET_KEY = '98fsdf882'
USER_COOKIE = 'auth'


def check_password(password, pass_token):
    sault = pass_token.split('|')[1]
    return generate_password_token(password, sault) == pass_token


def create_user(username, password, email):
    hash_sault = get_random_str()
    pass_token = generate_password_token(password, hash_sault)
    user = User(username=username, password=pass_token, email=email)
    user.put()

    return user.key().id()


def generate_password_token(password, sault):
    hashed_pass = hmac.new(sault, password).hexdigest()
    return '%s|%s' % (hashed_pass, sault)


def generate_auth_token(user_id):
    hashed_id = hmac.new(SECRET_KEY, str(user_id)).hexdigest()
    return '%s|%s' % (user_id, hashed_id)


def get_user_from_token(token):
    user_id = token.split('|')[0]
    if generate_auth_token(user_id) == token:
        return User.get_by_id(int(user_id))


def get_random_str(size=6):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))
