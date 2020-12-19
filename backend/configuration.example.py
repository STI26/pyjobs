import random

def random_key():
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(-_=+)'
    secure_random = random.SystemRandom()
    return ''.join(secure_random.sample(charset, 50))


APP_SECRET_KEY = random_key() # or use static secret_key
APP_DEBUG = True

DATABASE = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': '',               # Database name
    'USER': '',               # PostgreSQL username
    'PASSWORD': '',           # PostgreSQL password
    'HOST': 'localhost',      # Database server
    'PORT': '',               # Database port (leave blank for default)
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CORS_ALLOWED = ['http://localhost:8080', 'http://127.0.0.1:8080']
