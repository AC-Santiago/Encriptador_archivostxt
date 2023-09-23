from django.urls import path
from . import views

urlpatterns = [
    path("login/<str:user_name>", views.login, name="login"),
    path("register/", views.register, name="register"),
]
