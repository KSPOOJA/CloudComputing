from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()

def init_app(app):
  db.init_app(app)
  mail.init_app(app)
  login_manager.init_app(app)
  login_manager.login_view = 'auth_routes.login'
