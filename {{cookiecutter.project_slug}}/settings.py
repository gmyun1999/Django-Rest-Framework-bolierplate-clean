{% raw %}


from pathlib import Path
import environ


# Initialize environment variables
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(env_file=BASE_DIR / ".env")

# Environment Settings
ENV = env("ENV", default="localhost")
SECRET_KEY = env("SECRET_KEY", default="")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])

# Logging Settings
LOG_FILE = BASE_DIR / "logs/debug.log"
LOG_FILE.parent.mkdir(exist_ok=True)
LOG_FILE.touch(exist_ok=True)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "{levelname} {asctime} {module} || {message}", "style": "{"},},
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": LOG_FILE,
            "maxBytes": 5 * 1024 * 1024,
            "backupCount": 10,
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "django": {"handlers": ["file", "console"], "level": "INFO", "propagate": True},
    },
}

# Installed Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
]

# Middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL Configuration
ROOT_URLCONF = "{{cookiecutter.project_name}}.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI Application
WSGI_APPLICATION = "{{cookiecutter.project_name}}.wsgi.application"

# Database Configuration
{% if cookiecutter.db_engine == "1" %}
# PostgreSQL Configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "macroAdmin",
        "PASSWORD": env("DB_PASSWORD", default=""),
        "HOST": env("DB_HOST", default=""),
        "PORT": "5432",
        "OPTIONS": {
            "options": "-c search_path=public,content",
        },
        "POOL_OPTIONS": {
            "POOL_SIZE": 30,
            "MAX_OVERFLOW": 10,
            "RECYCLE": 90,
            "PRE_PING": True,
        },
    }
}
{% elif cookiecutter.db_engine == "2" %}
# MySQL Configuration
import pymysql
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME", default="macro_db"),
        "USER": env("DB_USER", default="macroAdmin"),
        "PASSWORD": env("DB_PASSWORD", default=""),
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="3306"),
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
{% elif cookiecutter.db_engine == "3" %}
# MongoDB Configuration
DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": env("DB_NAME", default="DB_NAME"),
        "ENFORCE_SCHEMA": False,  # 기본적으로 False, 명시적 사용 권장
        "CLIENT": {
            "host": env("DB_HOST", default="mongodb://localhost:27017"),
            "username": env("DB_USER", default=""),
            "password": env("DB_PASSWORD", default=""),
            "authSource": env("DB_AUTH_SOURCE", default="admin"),
            "authMechanism": env("DB_AUTH_MECHANISM", default="SCRAM-SHA-1"),  # 기본 인증 메커니즘
        },
    }
}

{% else %}
raise ValueError("Invalid DB_ENGINE value. Use 1 for Postgres, 2 for MySQL, or 3 for MongoDB.")
{% endif %}

# Static Files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Language and Time Zone
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = True

# Default Primary Key
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DefaultContext.rounding = ROUND_HALF_UP
{% endraw %}