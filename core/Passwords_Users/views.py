import bcrypt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .cryptography_module import decrypt_password, encrypt_password
from .forms import PasswordsUsersForm, MasterKeyForm
from .models import Passwords_users
from ..Users_EncrytedPage.models import Users_EncrytedPage as Users

llave = settings.KEY


# Create your views here.


# -------------------------PASSWORDS PAGE-------------------------#
@login_required
def passwords_page(request):
    passwords = Passwords_users.objects.filter(user=request.user)
    master_key = Users.objects.get(username=request.user).master_key
    cookie_pin = request.COOKIES.get("cookie_pin")

    if request.method == "POST":
        if "form_delete_password" in request.POST:
            delete_password(request)
        form = MasterKeyForm(request.POST)
        try:
            if not form.is_valid():
                return redirect("Passwords_Page")
            if not master_key:
                return create_pin(request)
            if not pin_validator(request):
                return redirect("Passwords_Page")
            if "form_password_detail" in request.POST:
                return redirect_to_password_detail(request)
            elif "form_create_password" in request.POST:
                return redirect_to_create_password(request)
        except ValueError:
            return redirect("Passwords_Page")

    elif request.method == "GET":
        if "form_find_password" in request.GET:
            passwords = find_password(request)
        passwords_exist = False if not passwords else True
        master_key_exist = True if master_key else False
        return render(
            request,
            "Passwords_page.html",
            {
                "passwords": passwords,
                "passwords_exist": passwords_exist,
                "master_key_exist": master_key_exist,
                "form": MasterKeyForm,
                "cookie_pin": cookie_pin,
            },
        )


# """Elimina la contraseña"""
def delete_password(request):
    password_id = request.POST.get("password_id")
    password = get_object_or_404(Passwords_users, pk=password_id, user=request.user)
    password.delete()
    return redirect("Passwords_Page")


# """Redirecciona a la página de detalle de contraseña"""
def redirect_to_password_detail(request):
    password_id = request.POST.get("password_id")
    response = redirect("password_detail", password_id=password_id)
    response.set_cookie("cookie_pin", "True")
    return response


# """Redirecciona a la página de crear contraseña"""
def redirect_to_create_password(request):
    response = redirect("Create_Password")
    response.set_cookie("cookie_pin", "True")
    return response


# """Hash la master key del usuario y la guarda en la base de datos"""
def hash_and_save_master_key(request, master_key):
    hashed_master_key = bcrypt.hashpw(str(master_key).encode("utf-8"), bcrypt.gensalt())
    Users.objects.filter(username=request.user).update(
        master_key=hashed_master_key.decode("utf-8")
    )


# """ Crea el pin del usuario """
def create_pin(request):
    master_key = request.POST.get("master_key")
    if master_key and len(str(master_key)) == 8:
        hash_and_save_master_key(request, master_key)
        response = redirect("Passwords_Page")
        return response


# """ Válida el pin del usuario"""
def pin_validator(request):
    if request.method == "POST":
        master_key: int = Users.objects.get(username=request.user).master_key
        form = MasterKeyForm(request.POST)
        try:
            if form.is_valid():
                pass
            if master_key:
                input_master_key = request.POST.get("master_key")
                resultado = bcrypt.checkpw(
                    str(input_master_key).encode("utf-8"),
                    str(master_key).encode("utf-8"),
                )
                return resultado
        except ValueError:
            return redirect("Passwords_Page")


# """"Busca la contraseña"""
def find_password(request):
    search = request.GET.get("search")
    query = Q(password_name__icontains=search) | Q(password_origin__icontains=search)
    query |= Q(password_username__icontains=search)
    passwords = Passwords_users.objects.filter(query, user=request.user)
    if not passwords:
        passwords = Passwords_users.objects.filter(user=request.user)
    return passwords


# -------------------------PASSWORDS PAGE--------------------------#


# -------------------------CREATE PASSWORD-------------------------#
@login_required
def create_password(request):
    if request.method == "POST":
        form = PasswordsUsersForm(request.POST)
        if form.is_valid():
            # extraemos los datos del formulario
            name = request.POST.get("password_name")
            username = request.POST.get("password_username")
            email = request.POST.get("password_email")
            origin = request.POST.get("password_origin")
            password = request.POST.get("password")

            # encriptamos la contraseña y el email
            encrypted_password = encrypt_password(password, llave)
            encrypted_email = encrypt_password(email, llave)

            # creamos el objeto
            new_password = Passwords_users(
                password_name=name,
                password_username=username,
                password_email=encrypted_email,
                password_origin=origin,
                password=encrypted_password,
                user=request.user,
            )
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


# -------------------------CREATE PASSWORD-------------------------#


# -------------------------PASSWORD DETAIL-------------------------#
@login_required
def password_detail(request, password_id):
    if request.method == "POST":
        password = get_object_or_404(Passwords_users, pk=password_id, user=request.user)
        form = PasswordsUsersForm(request.POST, instance=password)
        if form.is_valid():
            try:
                password.password = encrypt_password(
                    request.POST.get("password"), llave
                )
                password.password_email = encrypt_password(
                    request.POST.get("password_email"), llave
                )
                password.save()
                return redirect("Passwords_Page")
            except ValueError:
                return render(
                    request,
                    "password_detail.html",
                    {"password": password, "form": form, "error": "Invalid form"},
                )
    elif request.method == "GET":
        password = get_object_or_404(Passwords_users, pk=password_id, user=request.user)
        return render(
            request,
            "password_detail.html",
            {
                "password": password,
                "form": PasswordsUsersForm(instance=password),
                "password_email": decrypt_password(password.password_email, llave),
                "password_password": decrypt_password(password.password, llave),
            },
        )

# -------------------------PASSWORD DETAIL-------------------------#
