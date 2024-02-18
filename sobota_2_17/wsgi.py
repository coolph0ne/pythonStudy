# """
# WSGI config for sobota_2_17 project.
#
# It exposes the WSGI callable as a module-level variable named ``application``.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
# """

#import os
#
#from django.core.wsgi import get_wsgi_application
#
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sobota_2_17.settings")
#
#application = get_wsgi_application()

import os
import sys

path = '/home/coolph0ne/pythonStudy'
if path not in sys.path:
    sys.path.insert(0,path)

os.environ['DJANGO_SETTINGS_MODULE'] == 'sobota_2_17.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
