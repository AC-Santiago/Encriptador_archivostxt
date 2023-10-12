from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PasswordsUsersForm
from .models import Passwords_users


# Create your views here.
@login_required
def passwords_page(request):
    passwords = Passwords_users.objects.filter(user=request.user)
    print(passwords)
    if request.method == "POST":
        return render(request, "Passwords_page.html", {"passwords": passwords})
    elif request.method == "GET":
        return render(request, "Passwords_page.html", {"passwords": passwords})


@login_required
def create_password(request):
    if request.method == "POST":
        form = PasswordsUsersForm(request.POST)
        if form.is_valid():
            new_password = form.save(commit=False)
            new_password.user = request.user
            new_password.save()
            return redirect("Passwords_Page")
        else:
            return render(
                request,
                "CreatePasswords_page.html",
                {"form": PasswordsUsersForm, "error": "Invalid form"},
            )
    elif request.method == "GET":
        return render(
            request, "CreatePasswords_page.html", {"form": PasswordsUsersForm}
        )


@login_required
def password_detail(request, password_id):
    if request.method == "POST":
        password = get_object_or_404(Passwords_users, pk=password_id, user=request.user)
        form = PasswordsUsersForm(request.POST, instance=password)
        try:
            form.save()
            return redirect("Passwords_Page")
        except ValueError:
            return render(
                request,
                "password_detail.html",
                {"password": password, "form": form, "error": "Invalid form"},
            )
    elif request.method == "GET":
        password = get_object_or_404(Passwords_users, pk=password_id, user=request.user)
        form = PasswordsUsersForm(instance=password)
        return render(
            request,
            "password_detail.html",
            {"password": password, "form": form},
        )
