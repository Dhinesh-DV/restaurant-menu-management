"""
WSGI config for Restaurant_prj project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurant_prj.settings')

application = get_wsgi_application()
