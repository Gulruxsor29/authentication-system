import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'cyber-dev-secret-2024')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://root:@localhost/cyber_auth_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = 1800
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = 3600
