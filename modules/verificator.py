import re


class Verificator(object):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    PASSWORD_RE = re.compile(r"^.{3,20}$")
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

    FAIL_USER_NAME_MES = "That's not a valid username."
    FAIL_PASS_MESSAGE = "That wasn't a valid password."
    NOT_EQUAL_PASS_MES = "Your passwords didn't match."
    FAIL_EMAIL_MES = "That's not a valid email"

    @staticmethod
    def verify_name(username):
        return Verificator.USER_RE.match(username)

    @staticmethod
    def verify_equality_passwords(sourcePass, repitPass):
        return sourcePass == repitPass

    @staticmethod
    def verify_password(password):
        return Verificator.PASSWORD_RE.match(password)

    @staticmethod
    def verify_email(email):
        return email == "" or Verificator.EMAIL_RE.match(email)
