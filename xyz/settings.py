# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
INSTALLED_APPS = [
    'xyz',  # Add your app name here
 ]
TIME_ZONE = 'Africa/Nairobi'