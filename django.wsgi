import os
import sys
path = '/var/www/ProjectManager'
path2 = '/var/www/ProjectManager/mysite'
if path not in sys.path:
   sys.path.append(path)
if path2 not in sys.path:
   sys.path.append(path2)

os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()