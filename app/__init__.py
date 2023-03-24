from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__) # This is the name of the module
app.config['SECRET_KEY']= '6150293ab0b283698350acd7307257a2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db= SQLAlchemy(app)
login_manager= LoginManager(app)
login_manager.login_view= 'login' # account,....
login_manager.login_message_category= 'info' # account,....
from app import *

if __name__ == '__main__':
    db.create_all()

bcrypt = Bcrypt(app)
from app import routes
