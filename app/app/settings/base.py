"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'changemeplease')


# Application definition

INSTALLED_APPS = [
    # This project
    'website',
    'streams',
    # CodeRed CMS
    'coderedcms',
    'bootstrap4',
    'modelcluster',
    'taggit',
    'wagtailfontawesome',
    'wagtailcache',
    'wagtailimportexport',
    # Wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.core',
    'wagtail.contrib.settings',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.table_block',
    'wagtail.admin',
    'wagtailmedia',
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sitemaps",
]

MIDDLEWARE = [
    # Save pages to cache. Must be FIRST.
    'wagtailcache.cache.UpdateCacheMiddleware',
    # Common functionality
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Security
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # Error reporting. Uncomment this to recieve emails when a 404 is triggered.
    #'django.middleware.common.BrokenLinkEmailsMiddleware',
    # CMS functionality
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    # Fetch from cache. Must be LAST.
    'wagtailcache.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ]
        },
    }
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        'CONN_MAX_AGE': 0,
        "ENGINE": os.environ.get("DBENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DBNAME", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("DBUSER", "user"),
        "PASSWORD": os.environ.get("DBPASS", "password"),
        "HOST": os.environ.get("DBHOST", "localhost"),
        "PORT": os.environ.get("DBPORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Login

LOGIN_URL = 'wagtailadmin_login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'


# Wagtail settings

WAGTAIL_SITE_NAME = "Live Life"

WAGTAIL_ENABLE_UPDATE_CHECK = False

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://www.youdea.co.uk'


# Bootstrap

BOOTSTRAP4 = {
    # set to blank since coderedcms already loads jquery and bootstrap
    'jquery_url': '',
    'base_url': '',
    # remove green highlight on inputs
    'success_css_class': '',
}
import dj_database_url

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

REDIS_URL = os.environ.get('REDIS_URL')
if REDIS_URL is not None:
    CACHES = {'default': {'BACKEND': 'redis_cache.RedisCache', 'LOCATION': REDIS_URL}}  # in seconds
    WAGTAIL_CACHE = True
    import djcelery

    djcelery.setup_loader()

    CELERY_SEND_TASK_ERROR_EMAILS = True
    BROKER_URL = REDIS_URL

# Tags

TAGGIT_CASE_INSENSITIVE = True
