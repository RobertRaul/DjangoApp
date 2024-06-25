from pathlib import Path
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9$z0u!+78aa6#y+1x$m=z^=#us_)(mer=u6=h*c!p8w3h*ave@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

#TODO aplicaciones base, las que vienen por defecto
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
#TODO aplicaciones locales, las que yo creo
LOCAL_APPS = [
    'apps.base',
    'apps.users',
    'apps.products',    
    'apps.expense_manager',
]
#TODO aplicaciones de terceros, las que instalamos, librerias etc
THIRD_APPS = [
    'rest_framework',
    'simple_history',
    'drf_yasg', 
    'rest_framework.authtoken',
    'corsheaders',
    'rest_framework_simplejwt',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

SWAGGER_SETTINGS={
    'DOC_EXPANSION':'none',
}

#TODO instalamos SIMPLE JWT json web token  https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
#TODO  DEFAULT_PERMISSION_CLASSES con esto en cada vista pediran una autorización
REST_FRAMEWORK  = {    
    'DEFAULT_AUTHENTICATION_CLASSES': [        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (  
        'rest_framework.permissions.IsAuthenticated',
    ),
}

#TODO agregamos un tiempo de vida para el token, 1 dia para no generar cada rato
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS':True,
    'BLACKLIST_AFTER_ROTATION':True,
}



#TODO creamos una variabble donde se almacenara en cuanto tiempo expira el token
#TODO tiempo que pouede durar un toiken son 15 minutos = 900 segundos
#TOKEN_EXPIRED_AFTER_SECONDS = 900  -- Lo desactivamos ya que estamos usando SIMPLJWT

MIDDLEWARE = [
    #TODO agregamos este middleware lo mas arriba posible
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #TODO se agrega este middleware para la libreria django-simple-history
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'ecommerce_rest.urls'

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

WSGI_APPLICATION = 'ecommerce_rest.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#TODO Creamos nuestro modelo user asi que lo REESCRIBIMOS, ahora el user trabajar con este modelo
AUTH_USER_MODEL = 'users.User'

#TODO para trabajador con CORS instalamos del siguiente repo https://github.com/adamchainz/django-cors-headers
#TODO LUEGO agregamos estas configuraciones "rutas del FRONTED" para que puedan realizar las acciones de login list o update
CORS_ALLOWED_ORIGINS = [    
    "http://localhost:3000",    
]
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
]