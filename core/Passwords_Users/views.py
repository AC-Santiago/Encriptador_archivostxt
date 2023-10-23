from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import PasswordsUsersForm, MasterKeyForm
from .models import Passwords_users
from ..Users_EncrytedPage.models import Users_EncrytedPage as Users
from .cryptography_module import decrypt_password, encrypt_password
import bcrypt

llave = settings.KEY


# Create your views here.
@login_required
def passwords_page(request):
    passwords = Passwords_users.objects.filter(user=request.user)
    master_key: int = Users.objects.get(username=request.user).master_key
    cookie_pin = request.COOKIES.get("cookie_pin")
    if request.method == "POST":
        if "form_delete_password" in request.POST:
            password_id = request.POST.get("password_id")
            password = get_object_or_404(
                Passwords_users, pk=password_id, user=request.user
            )
            password.delete()
            return redirect("Passwords_Page")
        form = MasterKeyForm(request.POST)
        try:
            if form.is_valid():
                if master_key:
                    if pin_validator(request):
                        if "form_password_detail" in request.POST:
                            password_id = request.POST.get("password_id")
                            response = redirect(
                                "password_detail",
                                password_id=password_id,
                            )
                            response.set_cookie("cookie_pin", "True")
                            return response
                        elif "form_create_password" in request.POST:
                            response = redirect("Create_Password")
                            response.set_cookie("cookie_pin", "True")
                            return response

                    else:
                        return redirect("Passwords_Page")
                else:
                    master_key: int = request.POST.get("master_key")
                    if master_key and len(str(master_key)) == 8:
                        # le hacemos un hash a la master key
                        hashed_master_key = bcrypt.hashpw(
                            str(master_key).encode("utf-8"), bcrypt.gensalt()
                        )
                        # guardamos la master key en la base de datos
                        Users.objects.filter(username=request.user).update(
                            master_key=hashed_master_key.decode("utf-8")
                        )
                        return redirect("Passwords_Page")

        except ValueError:
            return redirect("Passwords_Page")

    elif request.method == "GET":
        if not passwords:
            passwords_exist = False
        else:
            passwords_exist = True
        if not master_key:
            master_key_exist = False
            return render(
                request,
                "Passwords_page.html",
                {
                    "passwords": passwords,
                    "passwords_exist": passwords_exist,
                    "master_key_exist": master_key_exist,
                    "form": MasterKeyForm,
                },
            )
        else:
            master_key_exist = True
            if cookie_pin:
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
            else:
                return render(
                    request,
                    "Passwords_page.html",
                    {
                        "passwords": passwords,
                        "passwords_exist": passwords_exist,
                        "master_key_exist": master_key_exist,
                        "form": MasterKeyForm,
                    },
                )


@login_required
def pin_validator(request):
    if request.method == "POST":
        master_key: int = Users.objects.get(username=request.user).master_key
        form = MasterKeyForm(request.POST)
        print(master_key)
        if form.is_valid():
            if master_key:
                input_master_key = request.POST.get("master_key")
                print(input_master_key)
                if bcrypt.checkpw(
                    str(input_master_key).encode("utf-8"),
                    str(master_key).encode("utf-8"),
                ):
                    print("La master key es correcta")
                    return True
                else:
                    print("La master key es incorrecta")
                    return False

    elif request.method == "GET":
        return redirect("Passwords_Page")


@login_required
def create_password(request):
    # obtiene la master key del usuario
    master_key = Users.objects.get(username=request.user).master_key
    print(master_key)
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
            print(encrypted_password)
            print(new_password)
            new_password.save()
            return redirect("Passwords_Page")
        else:
            return render(
                request,
                "CreatePasswords_page.html",
                {"form": PasswordsUsersForm, "error": "Invalid form"},
            )
    elif request.method == "GET":
        if master_key is None:
            return render(
                request,
                "CreatePasswords_page.html",
                {"form": PasswordsUsersForm},
            )
        else:
            return render(
                request, "CreatePasswords_page.html", {"form": PasswordsUsersForm}
            )


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
        form = PasswordsUsersForm(instance=password)
        password_decrypt = decrypt_password(password.password, llave)
        email_decrypt = decrypt_password(password.password_email, llave)
        return render(
            request,
            "password_detail.html",
            {
                "password": password,
                "form": form,
                "password_email": email_decrypt,
                "password_password": password_decrypt,
            },
        )
