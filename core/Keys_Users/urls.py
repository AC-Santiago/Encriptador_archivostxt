from django.urls import path

from . import views

urlpatterns = [
    path("Keys_Page/", views.keys_page, name="Keys_Page"),
    path("CreateKeys_Page/", views.create_keys, name="CreateKeys_Page"),
    path("KeyDetail_Page/<int:key_id>/", views.key_detail, name="KeyDetail_Page"),
]
