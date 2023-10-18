from django.db import models
from core.Users_EncrytedPage.models import Users_EncrytedPage


# Create your models here.
class Passwords_users(models.Model):
    user = models.ForeignKey(Users_EncrytedPage, on_delete=models.CASCADE)
    password_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password_username = models.CharField(max_length=100)
    password_email = models.CharField(max_length=200)
    password_origin = models.CharField(max_length=100)

    def __str__(self):
        return self.password_name + " " + self.user.username
