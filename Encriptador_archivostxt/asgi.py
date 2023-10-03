"""
ASGI config for Encriptador_archivostxt project.

It exposes the ASGI callable as rsa module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Encriptador_archivostxt.settings")

application = get_asgi_application()
