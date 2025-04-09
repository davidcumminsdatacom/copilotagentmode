# settings.py
# ...existing Django settings...

# MongoDB Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# CORS Configuration
INSTALLED_APPS += [
    'corsheaders',
    'octofit_tracker',
    'djongo'
]

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = ['*']

ALLOWED_HOSTS = ['*']
