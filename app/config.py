import os
class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT = 535
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'email@gmail.com'
    MAIL_PASSWORD = '*******'