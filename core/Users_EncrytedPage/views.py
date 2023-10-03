from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Users_EncrytedPage as Users


# Create your views here.
def register_page(request):
    if request.method == "POST":
        if request.POST["password"] != request.POST["password2"]:
            return render(
                request, "Register_U.html", {"error": "Passwords do not match"}
            )
        else:
            try:
                user = Users.objects.create_user(
                    username=request.POST["username"],
                    email=request.POST["email"],
                    password=request.POST["password"],
                )
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(
                    request, "Register_U.html", {"error": "Username already taken"}
                )

    elif request.method == "GET":
        return render(request, "Register_U.html")


def login_page(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "Login_U.html",
                {
                    "error": "Username and password did not match",
                    "form": AuthenticationForm,
                },
            )
        else:
            login(request, user)
            return redirect("home")
    elif request.method == "GET":
        return render(request, "Login_U.html", {"form": AuthenticationForm})


def sign_out(request):
    logout(request)
    return redirect("login")
