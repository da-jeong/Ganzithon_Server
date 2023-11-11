"""
Django settings for samsisekki project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e1uv#ba#6576+hwa3e1kukx8at)2udu#v1r_y822adysv&_+4a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'travelapp',
    'course',
    # django-rest-auth
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    # 'dj_rest_auth',

    # 'dj_rest_auth.registration',
    # 'rest_auth.registration',
    # 'rest_framework.authtoken',

    # django-allauth
    # 'allauth',
    # 'allauth.account',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'account.User'

CORS_ORIGIN_ALLOW_ALL = True # 모든 호스트 허용

CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
'djangorestframework_camel_case.render.CamelCaseJSONRenderer', 
'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
),
'DEFAULT_PARSER_CLASSES': (
'djangorestframework_camel_case.parser.CamelCaseFormParser', 
'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
'djangorestframework_camel_case.parser.CamelCaseJSONParser',
),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated', # 인증된 사용자만 접근
        # 'rest_framework.permissions.IsAdminUser', # 관리자만 접근
        'rest_framework.permissions.AllowAny', # 누구나 접근
    ),
}


from datetime import timedelta
# 추가적인 JWT_AUTH 설정
SIMPLE_JWT = {
    # 액세스 토큰이 유효한 기간을 지정
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    # 새로 고침 토큰이 유효한 기간을 지정
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    # 토큰에 대한 서명/확인 작업을 수행하는 데 사용되는 PyJWT 라이브러리의 알고리즘
    'ALGORITHM': 'HS256',
    # 생성된 토큰의 콘텐츠에 서명하는 데 사용되는 서명 키
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'userId',
    'USER_ID_CLAIM': 'userId',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'accounts.User',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


ROOT_URLCONF = 'samsisekki.urls'

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

WSGI_APPLICATION = 'samsisekki.wsgi.application'

# Email 전송
# 메일을 호스트하는 서버
EMAIL_HOST = 'smtp.gmail.com'

# gmail과의 통신하는 포트
EMAIL_PORT = '587'

# 발신할 이메일
EMAIL_HOST_USER = 'samsisekki333@gmail.com'
#EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")

# 발신할 메일의 비밀번호
EMAIL_HOST_PASSWORD = 'diel yprg nnvt kxfs'
#EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")

# TLS 보안 방법
EMAIL_USE_TLS = True

# 사이트와 관련한 자동응답을 받을 이메일 주소
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
