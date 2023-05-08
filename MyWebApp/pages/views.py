from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def home_view(*args, **kwargs):
#     return HttpResponse("<h1>Hello World</h1>") # String of HTML code


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    return render(request, "home.html", {})  # Call the templates dir with (home.html) inside and return it

    # return HttpResponse("<h1>Contact Page</h1>") # String of HTML code


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 321]
    }
    return render(request, "about.html", my_context)
