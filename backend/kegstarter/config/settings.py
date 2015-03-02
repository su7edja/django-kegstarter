"""
Django settings for kegstarter project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from configurations import Configuration, values

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Common(Configuration):
    SECRET_KEY = 'Immareallybadideatocheckintogithub,maybeyoushouldchangethis'
    DEBUG = True
    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []

    DJANGO_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    )

    THIRDPARTY_APPS = ()

    OUR_APPS = (
        'kegstarter.kegledger',
        'kegstarter.kegmanager',
        'kegstarter.votingbooth',
    )

    INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + OUR_APPS

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'kegstarter.config.urls'

    WSGI_APPLICATION = 'kegstarter.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.7/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/1.7/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = values.Value(os.path.abspath(os.path.join(BASE_DIR, '..', 'collected_static', '')))


class Local(Common):
    DATABASES = values.DatabaseURLValue('postgres://kegstarter:kegstarter@localhost:15432/kegstarter')


class Testing(Common):
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'  # Aka fake storage... sorta
    MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'tests', 'statics'))  # Store test tmp files here


class Prod(Common):
    DEBUG = False
    TEMPLATE_DEBUG = False

    SECRET_KEY = values.SecretValue()
