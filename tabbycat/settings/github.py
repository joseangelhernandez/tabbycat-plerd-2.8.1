# ==============================================================================
# Github CI
# ==============================================================================


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
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
