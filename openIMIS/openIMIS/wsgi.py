"""
WSGI config for openIMIS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'openIMIS.settings')

application = get_wsgi_application()

# Build the GraphQL schema now, at start-up. Built lazily by the first request instead, graphene's
# recursive walk over the types starts from the server thread's much deeper stack and can pass Python's
# recursion limit; the failed import is not cached, so every request then fails the same way.
import openIMIS.schema  # noqa: E402,F401
