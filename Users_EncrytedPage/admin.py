from django.contrib import admin
from .models import keys, passwords, users

# Register your models here.
admin.site.register(users)
admin.site.register(keys)
admin.site.register(passwords)
