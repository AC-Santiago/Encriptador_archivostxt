import bcrypt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from core.Dec_Cif.src.Funciones.Cifrado_decifrado import RSA
from core.Users_EncrytedPage.models import Users_EncrytedPage as Users
from .cryptography_module_keys import decrypt_keys, encrypt_keys
from .forms import MasterKeyForm, Keys_users_form
from .models import Keys_users

# Create your views here.
llave = settings.KEY


# -------------------------KEYS PAGE-------------------------#
@login_required
def keys_page(request):
    keys_users = Keys_users.objects.filter(user=request.user)
    cookie_pin = request.COOKIES.get("cookie_pin")
    master_key = Users.objects.get(username=request.user).master_key
    if request.method == "GET":
        if "form_find_key" in request.GET:
            keys_users = find_key(request)
        keys_users_exist = False if not keys_users else True
        master_key_exist = True if master_key else False
        return render(
            request,
            "Keys_page.html",
            {
                "keys_exist": keys_users_exist,
                "cookie": cookie_pin,
                "master_key_exist": master_key_exist,
                "keys": keys_users,
                "form": MasterKeyForm,
            },
        )
    elif request.method == "POST":
        form = MasterKeyForm(request.POST)
        if "delete_key" in request.POST:
            return delete_key(request)
        try:
            if not form.is_valid():
                return redirect("Keys_Page")
            if not master_key:
                return create_pin(request)
            if not pin_validator(request):
                return redirect("Keys_Page")
            if "form_create_keys" in request.POST:
                return redirect_to_create_keys(request)
            if "form_key_detail" in request.POST:
                return redirect_to_edit_keys(request)
        except ValueError:
            return redirect("Keys_Page")


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
            return redirect("Keys_Page")


# """Redirecciona a la página de crear las llaves"""
def redirect_to_create_keys(request):
    response = redirect("CreateKeys_Page")
    response.set_cookie("cookie_pin", "True")
    return response


# """Redirecciona a la página de editar las llaves"""
def redirect_to_edit_keys(request):
    key_id = request.POST.get("key_id")
    response = redirect("KeyDetail_Page", key_id=key_id)
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
        response = redirect("Keys_Page")
        return response


# """Elimina la llave"""
def delete_key(request):
    key_id = request.POST.get("key_id")
    key = get_object_or_404(Keys_users, pk=key_id, user=request.user)
    key.delete()
    return redirect("Keys_Page")


# """Busca la llave"""
def find_key(request):
    consulta = request.GET.get("search")
    query = Q(key_name__icontains=consulta)
    keys_users = Keys_users.objects.filter(query)
    if not keys_users:
        keys_users = Keys_users.objects.filter(user=request.user)
    return keys_users


# -------------------------KEYS PAGE-------------------------#


# -------------------------CREATE KEYS PAGE-------------------------#
@login_required
def create_keys(request):
    if request.method == "GET":
        form = Keys_users_form()
        return render(request, "CreateKeys_page.html", {"form_keys": form})
    elif request.method == "POST":
        if "form_create_key" in request.POST:
            rsa = RSA()
            keys = rsa.generar_clave()
            try:
                new_key_name = request.POST.get("key_name")
                new_key_public = encrypt_keys(str(keys[0]), llave)
                new_key_private = encrypt_keys(str(keys[1]), llave)

                new_key = Keys_users(
                    user=request.user,
                    key_name=new_key_name,
                    key_public=new_key_public,
                    key_private=new_key_private,
                )
                new_key.save()
                return redirect("Keys_Page")
            except ValueError:
                return redirect("Keys_Page")
        return redirect("Keys_Page")


# -------------------------CREATE KEYS PAGE-------------------------#

# -----------------------KEY DETAILS PAGE-----------------------#
@login_required
def key_detail(request, key_id):
    if request.method == "GET":
        key = get_object_or_404(Keys_users, pk=key_id, user=request.user)
        form = Keys_users_form(instance=key)
        return render(request, "Key_detail.html",
                      {"key": key, "key_public": decrypt_keys(key.key_public, llave),
                       "key_private": decrypt_keys(key.key_private, llave), "form_keys": form})
    elif request.method == "POST":
        if "form_edit_key" in request.POST:
            key = get_object_or_404(Keys_users, pk=key_id, user=request.user)
            form = Keys_users_form(request.POST, instance=key)
            try:
                key.key_public = encrypt_keys(request.POST.get("key_public"), llave)
                key.key_private = encrypt_keys(request.POST.get("key_private"), llave)
                key.save()
                return redirect("Keys_Page")
            except ValueError:
                return redirect("Keys_Page")
