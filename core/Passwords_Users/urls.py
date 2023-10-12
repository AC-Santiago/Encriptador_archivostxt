from django.urls import path
from . import views

urlpatterns = [
    path("passwords/", views.passwords_page, name="Passwords_Page"),
    path("create/", views.create_password, name="Create_Password"),
    path("password/<int:password_id>/", views.password_detail, name="password_detail"),
]
