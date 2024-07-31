from .base import *

DEBUG = True

SECRET_KEY = "$40qmb+2vk+*5jfb(l%!838gfr(-uoo3&&038#(!amxsqib+9u"

ALLOWED_HOSTS = ["ferrariluisa.com", "www.ferrariluisa.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ferrariluisa_prod',
        'USER': 'ferrariluisa',
        'PASSWORD': 'Ct2x76EySI9U',
        'HOST': 'localhost',
        'PORT': ''
    }
}


try:
    from .local import *
except ImportError:
    pass
