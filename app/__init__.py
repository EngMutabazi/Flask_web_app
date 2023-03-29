from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config

# app = Flask(__name__) # This is the name of the module
# # app.config['SECRET_KEY']= '6150293ab0b283698350acd7307257a2'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config.from_object(Config)
db= SQLAlchemy()
bcrypt = Bcrypt()
login_manager= LoginManager()
login_manager.login_view= 'users.login' # account,....
login_manager.login_message_category= 'info' # account,....


# app.config['MAIL_SERVER']='smtp.googlemail.com'
# app.config['MAIL_PORT'] = 535
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'email@gmail.com'
# app.config['MAIL_PASSWORD'] = '*******'
mail = Mail()

from app import *
if __name__ == '__main__':
    db.create_all()
    bcrypt = Bcrypt()

# importing routes 
# from app.users.routes import users
# from app.posts.routes import posts
# from app.main.routes import main
# from app.errors.handlers import errors
# app.register_blueprint(users)
# app.register_blueprint(posts)
# app.register_blueprint(main)
# app.register_blueprint(errors)

def create_app(config_class= Config):
    app = Flask(__name__) 
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from app.users.routes import users
    from app.posts.routes import posts
    from app.main.routes import main
    from app.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    return app
