"""
ASGI config for ecommerce_rest project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
#TODO agregamos el .local ya que buscara la carpeta settigs y luego el archivo local
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_rest.settings.local')

application = get_asgi_application()
