from django.contrib.auth.backends import BaseBackend 
from .models import User
class Email_type(BaseBackend):

    def authenticate(self , request , username = None , password = None):
        try:
            person = User.objects.get(email = username)
            print(person)
            if person.check_password(password):
                return person
            else:
                return None
        except:
            return None
    def get_user(self , user_id):
        try:
            return User.objects.get(pk = user_id)
        except:
            return None
            