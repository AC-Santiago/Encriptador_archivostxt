from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("dec_cif/", views.dec_cif, name="dec_cif"),
]
