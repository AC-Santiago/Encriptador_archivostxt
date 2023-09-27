from django.urls import path
from . import views

urlpatterns = [
    path("Keys_Page/", views.Keys_Page, name="Keys_Page"),
]
