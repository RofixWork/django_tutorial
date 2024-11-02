import re

from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse


class CheckUserAuth:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if (
            re.match("(/students/)+", request.path)
            and not request.user.is_authenticated
        ):
            return HttpResponseRedirect(reverse("login"))
        response = self.get_response(request)

        return response
