"""
WSGI config for boutique_ado project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boutique_ado.settings')



application = get_wsgi_application()
