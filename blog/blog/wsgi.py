"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

#Añade la ruta de tu proyecto al sys.path
path = '/home/GrupoSiete/G7News/blog'
if path not in sys.path:
    sys.path.append(path)

#Establece el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.production')

#Obtiene la aplicación WSGI
application = get_wsgi_application()