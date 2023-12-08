import json
import os
from pathlib import Path

from django.core.checks import Error, register


_settings_check_tag = "settings"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

placeholder_secret_key = "kick me"
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", placeholder_secret_key)

DEBUG = json.loads(os.getenv("DJANGO_DEBUG", "false"))


@register(_settings_check_tag)
def check_secret_key(app_configs, **kwargs):
    from django.conf import settings

    errors = []

    if not settings.DEBUG and settings.SECRET_KEY == placeholder_secret_key:
        errors.append(Error(
            "you must set `DJANGO_SECRET_KEY` outside of local dev",
            id="_.settings",
        ))

    return errors


default_allowed_hosts = "[\"*\"]" if DEBUG else "[]"
ALLOWED_HOSTS = json.loads(os.getenv(
    "DJANGO_ALLOWED_HOSTS",
    default_allowed_hosts,
))
CSRF_TRUSTED_ORIGINS = json.loads(os.getenv(
    "DJANGO_CSRF_TRUSTED_ORIGINS",
    "[]",
))

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "capabilities",
    "sendfile",
    "wait_for_db",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
]

ROOT_URLCONF = "_.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

FORM_RENDERER = "django.forms.renderers.DjangoDivFormRenderer"

WSGI_APPLICATION = "_.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("DJANGO_DATABASES_HOST"),
        "USER": os.getenv("DJANGO_DATABASES_USER"),
        "PASSWORD": os.getenv("DJANGO_DATABASES_PASSWORD"),
        "NAME": os.getenv("DJANGO_DATABASES_NAME"),
        "OPTIONS": {
            "options": f"-csearch_path={os.getenv('DJANGO_DATABASES_SCHEMA')}",
        },
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

_missing = object()

_caches = os.getenv("DJANGO_CACHES", _missing)
if _caches is not _missing:
    CACHES = json.loads(_caches)

_email_host = os.getenv("DJANGO_EMAIL_HOST", _missing)
if _email_host is not _missing:
    EMAIL_HOST = _email_host

_email_port = os.getenv("DJANGO_EMAIL_PORT", _missing)
if _email_port is not _missing:
    EMAIL_PORT = _email_port


AUTH_PASSWORD_VALIDATORS = json.loads(os.getenv(
    "DJANGO_AUTH_PASSWORD_VALIDATORS",
    "[]",
))


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = os.getenv("DJANGO_LANGUAGE_CODE", "en-gb")

TIME_ZONE = os.getenv("DJANGO_TIME_ZONE", "UTC")

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = "/static/"

_static_root = os.getenv("DJANGO_STATIC_ROOT", _missing)
if _static_root is not _missing:
    STATIC_ROOT = _static_root

_media_root = os.getenv("DJANGO_MEDIA_ROOT", _missing)
if _media_root is not _missing:
    MEDIA_ROOT = _media_root


@register(_settings_check_tag)
def check_media_root(app_configs, **kwargs):
    from django.conf import settings

    errors = []

    def can_write_at(root):
        with open(Path(root) / ".write-test", "w"):
            return True

        return False

    if not can_write_at(settings.MEDIA_ROOT):
        errors.append(Error(
            "you must set `DJANGO_MEDIA_ROOT` to a writeable path",
            id="_.settings",
        ))

    return errors


LOGOUT_REDIRECT_URL = "/"

ADMINS = json.loads(os.getenv("DJANGO_ADMINS", "[]"))
