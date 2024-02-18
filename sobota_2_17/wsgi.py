# """
# WSGI config for sobota_2_17 project.
#
# It exposes the WSGI callable as a module-level variable named ``application``.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
# """
#
# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sobota_2_17.settings")
#
# application = get_wsgi_application()


# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

#
## assuming your django settings file is at '/home/nazwauzytkownika/mysite/mysite/settings.py'
## and your manage.py is is at '/home/nazwauzytkownika/mysite/manage.py'
path = '/home/coolph0ne/pythonStudy'
if path not in sys.path:
    sys.path.append(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'sobota_2_17.settings'
#
## then:
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
##
#import django.core.handlers.wsgi
#
#application = django.core.handlers.wsgi.WSGIHandler()
