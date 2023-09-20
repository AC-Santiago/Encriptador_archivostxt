from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def login(request):
    name_user = str("santiago")
    return render(request, "Login_U.html", {"name_user": name_user})


def register(request):
    return HttpResponse("<h1>Register Page</h1>")
