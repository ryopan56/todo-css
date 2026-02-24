# flask_todo/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv

login_manager = LoginManager()
login_manager.login_view = 'todo_app.login'
login_manager.login_message = 'ログイン未完了です'

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    load_dotenv(override=False)
    
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    
    db_uri = os.getenv("SQLALCHEMY_DATABASE_URI")
    if not db_uri:
        raise RuntimeError("SQLALCHEMY_DATABASE_URI is not set in .env")

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from flask_todo.views import bp
    
    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    return app
