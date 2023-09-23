from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def login(request, user_name):
    name_user = user_name
    return render(request, "Login_U.html", {"name_user": name_user})


def register(request):
    return HttpResponse("<h1>Register Page</h1>")


def keys(request):
    return HttpResponse("<h1>Keys Page</h1>")


def passwords(request):
    return HttpResponse("<h1>Password Page</h1>")
