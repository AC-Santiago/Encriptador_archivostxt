from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("keys/", views.keys_page, name="keys"),
    path("passwords/", views.passwords_page, name="passwords"),
    path("register/", views.register, name="register"),
]
