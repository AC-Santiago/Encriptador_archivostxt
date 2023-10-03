from django.shortcuts import render
from .forms import PasswordsUsersform


# Create your views here.
def Passwords_page(request):
    return render(request, "Passwords_page.html")


def Create_Password(request):
    if request.method == "POST":
        form = PasswordsUsersform(request.POST)
        if form.is_valid():
            new_password = form.save(commit=False)
            new_password.user = request.user
            new_password.save()
            print("Valido")
            return render(request, "Passwords_page.html", {"form": PasswordsUsersform})
        else:
            return render(
                request,
                "CreatePasswords_page.html",
                {"form": PasswordsUsersform, "error": "Invalid form"},
            )
    else:
        return render(
            request, "CreatePasswords_page.html", {"form": PasswordsUsersform}
        )
