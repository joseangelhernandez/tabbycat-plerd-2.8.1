# ==============================================================================
# Github CI
# ==============================================================================
# ==============================================================================
# Settings that you should specify
# ==============================================================================

# SQL SERVER ENGINE

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'tabbyplerd',
        'USER': 'joseangel',
        'PASSWORD': 'Mejoan199',
        'HOST': 'pruebasplerd.database.windows.net',
        'PORT': '',

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'extra_params': 'TrustServerCertificate=yes;',
        },
    }
}

# Replace this with your time zone, as defined in the IANA time zone database:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
TIME_ZONE = 'Australia/Melbourne'


# ==============================================================================
# Django-specific Modules
# ==============================================================================

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1'
)

# ==============================================================================
# Caching
# ==============================================================================

PUBLIC_FAST_CACHE_TIMEOUT   = 0
PUBLIC_SLOW_CACHE_TIMEOUT   = 0
TAB_PAGES_CACHE_TIMEOUT     = 0

CACHES = { # Use a dummy cache in development
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
   }
}

# Use the cache with database write through for local sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'