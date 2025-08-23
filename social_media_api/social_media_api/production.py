
from .settings import *

#interact with the operating system
import os

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'your_server_ip_address']

# On your server, you will need to set an environment variable named 'DJANGO_SECRET_KEY'.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')


import dj_database_url

DATABASES = {
    
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'), conn_max_age=600)
}


SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True  
SESSION_COOKIE_SECURE = True 
CSRF_COOKIE_SECURE = True  
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')