# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nal_db',
        'USER': 'nal_db',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j^6x0_oo_&r9*hv&8goa7-dw63!c8k8tzo^#u1yhvsrlw9w@hq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']