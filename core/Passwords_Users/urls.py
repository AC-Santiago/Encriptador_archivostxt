from django.urls import path
from . import views

urlpatterns = [
    path("passwords/", views.Passwords_page, name="Passwords_Page"),
    path("create/", views.Create_Password, name="Create_Password"),
]
