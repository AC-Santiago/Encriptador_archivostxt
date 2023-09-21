from django.db import models


# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class keys(models.Model):
    public_key = models.CharField(max_length=200)
    private_key = models.CharField(max_length=200)
    user = models.ForeignKey(users, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class passwords(models.Model):
    origen = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    correo_electronico = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user = models.ForeignKey(users, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
