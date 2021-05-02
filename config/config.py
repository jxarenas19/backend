import os


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'ZG1WbWJHRjBMV3RwWlhKdkttTnZiRzl0WW1saEl6RXlNelExTmpjNE9UQWpNalZ0'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5433/prueba3'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://u406650721_marketing:Mnbv21.*@213.190.6.64/u406650721_dba24'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_SQLALCHEMY_LOG_MESSAGES = False
    API_PROTOCOL = 'http://'


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = os.getenv('DEBUG', False)
    TESTING = os.getenv('TESTING', False)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    API_PROTOCOL = os.getenv('API_PROTOCOL', 'https://')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    SHOW_SQLALCHEMY_LOG_MESSAGES = os.getenv('SHOW_SQLALCHEMY_LOG_MESSAGES', False)


app_config = {
    'development': Development,
    'production': Production,
}
