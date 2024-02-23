import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

SECRET_KEY = os.getenv('SECRET_KEY')


# DEBUG = os.getenv('DEBUG') == 'yes'
DEBUG = True

ALLOWED_HOSTS = ['testserver', 'webserver', '127.0.0.1', '0.0.0.0',
                 'localhost', 'python-project-52-production-b3b8.up.railway.app']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    'django_extensions',
    'task_manager',
    'bootstrap4',
    'django_filters',
    'users.apps.UsersConfig',
    'statuses.apps.StatusesConfig',
    'tasks.apps.TasksConfig',
    'labels.apps.LabelsConfig',
    'workplaces.apps.WorkplaceConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

ROOT_URLCONF = 'task_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'task_manager.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
if DEBUG is False:
    os.getenv('DATABASE_URL')
    db_from_env = dj_database_url.config(conn_max_age=600)
    DATABASES['default'].update(db_from_env)

CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
    'https://127.0.0.1',
    'https://localhost',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 3,
        }
    }
]

AUTH_USER_MODEL = 'users.Users'

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Dushanbe'
USE_I18N = True
USE_TZ = True

LOCALE_URL = "locale/"
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# DEFAULT_AUTO_FIELD = 'django.db.models.py.BigAutoField'
# DEFAULT_AUTO_FIELD = 'django.db.models.py.BigAutoField'

ROLLBAR = {
    'access_token': os.getenv('ACCESS_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}

BOOTSTRAP4 = {

    # The complete URL to the Bootstrap CSS file
    # Note that a URL can be either a string,
    # e.g. "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css",
    # or a dict like the default value below.
    "css_url": {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css",
        "integrity": "sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap bundle JavaScript file
    "javascript_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js",
        "integrity": "sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap CSS theme file (None means no theme)
    "theme_url": None,

    # The URL to the jQuery JavaScript file (full)
    "jquery_url": {
        "url": "https://code.jquery.com/jquery-3.5.1.min.js",
        "integrity": "sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2",
        "crossorigin": "anonymous",
    },

    # The URL to the jQuery JavaScript file (slim)
    "jquery_slim_url": {
        "url": "https://code.jquery.com/jquery-3.5.1.slim.min.js",
        "integrity": "sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj",
        "crossorigin": "anonymous",
    },

    # Put JavaScript in the HEAD section of the HTML document
    # (only relevant if you use bootstrap4.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript False|falsy|slim|full (default=False)
    # False - means tag bootstrap_javascript use default value -
    # `falsy` and does not include jQuery)
    'include_jquery': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-3',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-9',

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'is-invalid',

    # Class to indicate success, meaning the field has valid input
    # (better to set this in your Django form)
    'success_css_class': 'is-valid',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers': {
        'default': 'bootstrap4.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap4.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap4.renderers.FieldRenderer',
        'inline': 'bootstrap4.renderers.InlineFieldRenderer',
    },
}
