import os

from flask_appbuilder.security.manager import (
    AUTH_DB,
    AUTH_LDAP,
    AUTH_OAUTH,
    AUTH_OID,
    AUTH_REMOTE_USER
)

# Superset specific config
#---------------------------------------------------------
ROW_LIMIT = 5000
SUPERSET_WORKERS = 4
SUPERSET_WEBSERVER_PORT = 8088
SUPERSET_WEBSERVER_TIMEOUT = 240
SQLLAB_TIMEOUT = 240

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = False

# Set this API key to enable Mapbox visualization
#MAPBOX_API_KEY = ‘Miakey’
MAPBOX_API_KEY = os.getenv('SUPERSET_MAPBOX_API_KEY', '')

# Cache config
CACHE_CONFIG = {
  'CACHE_TYPE': 'redis',
  'CACHE_DEFAULT_TIMEOUT': 300,
  'CACHE_KEY_PREFIX': os.getenv('SUPERSET_REDIS_CACHE_PREFIX', 'superset_'),
  'CACHE_REDIS_HOST': os.getenv('SUPERSET_REDIS_HOST', 'redis'),
  'CACHE_REDIS_PORT': os.getenv('SUPERSET_REDIS_PORT', 6379),
  'CACHE_REDIS_DB': os.getenv('SUPERSET_REDIS_DB', 1),
  'CACHE_REDIS_URL': 'redis://%s:%s/%s' % (os.getenv('SUPERSET_REDIS_HOST', 'redis'), os.getenv('SUPERSET_REDIS_PORT', 6379), os.getenv('SUPERSET_REDIS_DB', 1))
}

# Postgres DB config
SQLALCHEMY_DATABASE_URI = \
  'postgresql+psycopg2://%s:%s@%s:%s/%s' % (os.getenv('SUPERSET_POSTGRES_USER', 'postgres'), os.getenv('SUPERSET_POSTGRES_PASS', 'postgres'), os.getenv('SUPERSET_POSTGRES_HOST', 'postgres'), os.getenv('SUPERSET_POSTGRES_PORT', 'port'), os.getenv('SUPERSET_POSTGRES_DB', 'superset'))

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.environ['SUPERSET_SECRET_KEY']

# Proxy for Load Balancer
ENABLE_PROXY_FIX = True

# Debug option
DEBUG = os.environ['SUPERSET_DEBUG']
LOG_LEVEL = os.environ['SUPERSET_DEBUG_LEVEL']

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------

# Uncomment to setup Full admin role name
AUTH_ROLE_ADMIN = 'Admin'

# Will allow users self registration
AUTH_USER_REGISTRATION = os.environ['SUPERSET_ENABLE_USER_REGISTRATION']

# Values could be AUTH_DB or AUTH_LDAP
AUTH_TYPE = os.environ['SUPERSET_AUTH_TYPE']

# LDAP config
AUTH_LDAP_SERVER = os.environ['SUPERSET_LDAP_URI']
AUTH_LDAP_SEARCH = os.environ['SUPERSET_LDAP_BASE_DN']
AUTH_LDAP_UID_FIELD = os.environ['SUPERSET_LDAP_UID_FIELD']
AUTH_LDAP_FIRSTNAME_FIELD = os.environ['SUPERSET_LDAP_FIRST_NAME_FIELD']
AUTH_LDAP_LASTNAME_FIELD = os.environ['SUPERSET_LDAP_LAST_NAME_FIELD']
AUTH_LDAP_EMAIL_FIELD = os.environ['SUPERSET_LDAP_EMAIL_FIELD']
AUTH_LDAP_BIND_USER = os.environ['SUPERSET_LDAP_BIND_USER']
AUTH_LDAP_BIND_PASSWORD = os.environ['SUPERSET_LDAP_BIND_PASS']
AUTH_LDAP_ALLOW_SELF_SIGNED = os.environ['SUPERSET_LDAP_ALLOW_SELF_SIGNED']

# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = 'en'
# Your application default translation path
BABEL_DEFAULT_FOLDER = 'babel/translations'
# The allowed translation for you app
LANGUAGES = {
  'en': {'flag': 'us', 'name': 'English'},
  'it': {'flag': 'it', 'name': 'Italian'}
}
