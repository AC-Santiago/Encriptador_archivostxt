from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Users_EncrytedPage(AbstractUser):
    image_profile = models.ImageField(upload_to="images/", null=True, blank=True)

    # se agrega un campo para el guardar la clave maestra del usuario
    master_key = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return self.username

    def get_image(self):
        if self.image_profile:
            return self.image_profile.url
        else:
            return "/static/images/default.png"
