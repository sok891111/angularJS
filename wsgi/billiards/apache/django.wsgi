 import os
 import sys
 
 path = '/home/sungjin/workspace/billiards/'    
 if path not in sys.path:
     sys.path.append(path)

 os.environ['DJANGO_SETTINGS_MODULE'] = 'billiards.settings'  

 import django.core.handlers.wsgi
 application = django.core.handlers.wsgi.WSGIHandler()