"""
WSGI config for social_media_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
sys.path.append('/home/sktakyi/Alx_DjangoLearnLab/social_media_api')

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'social_media_api.settings'

# Activate virtualenv
activate_this = '/home/sktakyi/Alx_DjangoLearnLab/.venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

