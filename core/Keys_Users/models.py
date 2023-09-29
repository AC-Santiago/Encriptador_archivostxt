from django.db import models

from core.Users_EncrytedPage.models import Users_EncrytedPage


# Create your models here.
class Keys_users(models.Model):
    user = models.ForeignKey(Users_EncrytedPage, on_delete=models.CASCADE)
    key_name = models.CharField(max_length=100)
    key_public = models.CharField(max_length=200)
    key_private = models.CharField(max_length=200)

    def __str__(self):
        return self.key_name + ' ' + self.user.username