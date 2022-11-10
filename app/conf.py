from app import app


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "hdhddhhdihbqekg"

    DB_NAME = "production_db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"

    UPLOADS = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True


class DevelopmentConfig(Config):
    app.secret_key = 'your secret key'

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'your password'
    app.config['MYSQL_DB'] = 'geeklogin'
