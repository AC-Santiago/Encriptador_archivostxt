from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, "Register_U.html")

def login(request):
    name_user = "Toby2003"
    return render(request, "Login_U.html", {"name_user": name_user})
