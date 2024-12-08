from functools import wraps
from django.http import HttpResponseRedirect
from django.urls import reverse
def logedin(func):
    @wraps(func)
    def wrapper(*args , **kwargs):
        if args[0].user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        else:
            return func(*args , **kwargs)

    return wrapper