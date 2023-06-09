from __future__ import absolute_import, unicode_literals

import environ
import os

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('agarwood')

env = environ.Env()
env.read_env()

ENVIRONMENT = env('ENVIRONMENT', default='development')

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres:///agarwood'),
}

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Admin
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'ckeditor',
    'ckeditor_uploader',
    'meta',
)

THIRD_PARTY_APPS = (
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'rest_framework',
    'social_django',  # social login
    'leaflet',
)

LOCAL_APPS = (
    # custom users app
    'agarwood.users.apps.UsersConfig',
    'agarwood.apps.apps.AppsConfig',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
# MIGRATION_MODULES = {
#     'sites': 'cleaner.contrib.sites.migrations'
# }

WSGI_APPLICATION = 'configs.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [('Thanh La', 'lavanthanh.1995@gmail.com'), ]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# Custom user app defaults
# Select the correct user model
# AUTH_USER_MODEL = 'users.CustomUser'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            # 'loaders': [
            #     'django.template.loaders.filesystem.Loader',
            #     'django.template.loaders.app_directories.Loader',
            # ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = env('SITE_ID', default=1)


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

PHOTOS_DIR_NAME = 'photos'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
#MEDIA_ROOT = str(APPS_DIR('media'))


#MEDIA_ROOT = '/home/vu/media'
MEDIA_ROOT = str(APPS_DIR.path('media'))
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# Custom user app defaults
# Select the correct user model
# AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login"
LOGIN_URL = '/admin/login'

#LOGOUT_REDIRECT_URL = 'home'
# ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login"
# LOGOUT_REDIRECT_URL = 'home'
# ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/logout"
# LOGIN_URL = 'account_logout'
# LOGIN_TWO_FACOR_URL ='two-factor-login'
# LOGIN_TWO_FACOR_REDIRECT_URL = 'home'


# Reset Password
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='admin@gmail.com')
SERVER_EMAIL = env('SERVER_EMAIL', default='admin@gmail.com')
EMAIL_PORT = env('EMAIL_PORT', default='587')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='admin@gmail.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='12345678x@X')


# Configuring the project in the backend
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', default='12345678x@X')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', default='12345678x@X')

SOCIAL_AUTH_FACEBOOK_KEY = env('SOCIAL_AUTH_FACEBOOK_KEY', default='12345678x@X')        # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = env('SOCIAL_AUTH_FACEBOOK_SECRET', default='12345678x@X')  # App Secret

# List permission in cleaner
LIST_PERMISSION = env.list('LIST_PERMISSION', default='superAdmin')

# SEO WEB FOR DJANGO
META_SITE_PROTOCOL = env('META_SITE_PROTOCOL', default='http')
META_SITE_DOMAIN = env('META_SITE_DOMAIN', default='localhost:8002')


# from meta.views import Meta

# meta = Meta(
#     title="Agarwood Co",
#     description='Product form Agarwood, Oud',
#     keywords=['Agarwood', 'Oud'],
#     extra_props = {
#         'viewport': 'width=device-width, initial-scale=1.0, minimum-scale=1.0'
#     },
#     extra_custom_props=[
#         ('http-equiv', 'Content-Type', 'text/html; charset=UTF-8'),
#     ],
#     use_sites=True
# )

# CK EDITOR CONFIG
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}