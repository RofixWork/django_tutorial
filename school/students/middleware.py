from django.http import HttpRequest, HttpResponse
from django.urls import reverse


def CustomFunctionMiddleware(get_response):
    print("config and initialization")

    def middleware(request):
        print("Before Called View")
        response = get_response(request)
        print("After Called View")
        return response

    return middleware


class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        print("Init...")

    def __call__(self, request: HttpRequest):
        if request.path == reverse("students.auth"):
            if request.GET.get("name") != "ahmed":
                return HttpResponse("Who are you?")

        response = self.get_response(request)
        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print("*" * 100)
    #     print("Before CALL VIEW")
    #     print("Path", request.path)
    #     print("Method", request.method)
    #     print("Func", view_func.__name__)
    #     print("*" * 100)
    #     return None

    # def process_exception(self, request, exception: Exception):
    #     print("*" * 90)
    #     print("SET VIEW HAVE A EXCEPTION")
    #     print("Exception", exception)
    #     print("*" * 90)
    #     return None
