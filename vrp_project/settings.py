# vrp_project/settings.py

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'YOUR_SECRET_KEY'

# Disable debug mode in production
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.sessions',    # Required for session management
    'django.contrib.messages',    # Required for messaging
    'vrp_app',                    # Your VRP application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',    # Session management
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',               # CSRF protection
    'django.contrib.messages.middleware.MessageMiddleware',     # Messaging framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vrp_project.urls'

# vrp_project/settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'vrp_app', 'templates')],  # Ensure this path is correct
        'APP_DIRS': True,  # Allows Django to look for templates inside each app's templates directory
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'vrp_project.wsgi.application'

# Database
# Using SQLite with an in-memory database to avoid file-based storage
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # Use in-memory database
    }
}

# Password validation
# Not needed as we're not using Django's auth system
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Session configuration to use signed cookies instead of database
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# Disable unnecessary middleware or apps that require the database
# Already handled by limiting INSTALLED_APPS
