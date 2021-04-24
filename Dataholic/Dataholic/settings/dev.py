from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd&m285#c7-9lsd^5ftu2r0e^)gagtqp52w(y50u9z2k$xual01'

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
