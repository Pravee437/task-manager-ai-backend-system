
#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from dotenv import load_dotenv
from .config import Config

load_dotenv()

db = SQLAlchemy()
mail = Mail()
migrate = Migrate()

def create_app(config_class=Config):  # Accept custom config class
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    from .routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
