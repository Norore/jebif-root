# -*- coding: utf-8

import os

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_SUBJECT_PREFIX = "[JeBiF] "

DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(PROJECT_PATH, 'database.sqlite3'),
                    'USER': '',
                    'PASSWORD': '',
                    'HOST': '',
                    'PORT': '',
                }
            }

ADMIN_TEMPLATE_DIR = "/var/lib/django/contrib/admin/templates"
ADMIN_MEDIA_ROOT = ""
from jebif.localsettings import *

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-FR'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_PATH + '/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/' + ROOT_URL + 'media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/' + ROOT_URL + 'admin_media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'middleware.RequireLoginMiddleware',
    'middleware.HttpMethodsMiddleware',
    'middleware.TerminalLogging'
)

ROOT_URLCONF = 'jebif.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_PATH + "/templates",
    PROJECT_PATH + "/cv/templates",
    ADMIN_TEMPLATE_DIR
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'cv.registration',
    'cv.candidate',
    'cv.users',
    'membership',
    'election',
)

AUTH_PROFILE_MODULE = 'users.UserProfile'
DATE_FORMAT = 'd/m/Y'
DATE_INPUT_FORMAT = '%d/%m/%Y'

#LOGIN_URL = "/%saccounts/login/" % ROOT_URL
LOGIN_URL = "/%saccounts/login/" % ROOT_URL
LOGIN_REDIRECT_URL = "/%smembership/subscription/me/update/" % ROOT_URL
REQUIRE_LOGIN_PATH = LOGIN_URL

