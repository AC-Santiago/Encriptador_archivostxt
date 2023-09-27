from django.urls import path
from . import views

urlpatterns = [
    path("Keys_Page/", views.Passwords_page, name="Passwords_Page"),
]
