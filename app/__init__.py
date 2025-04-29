import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap4
from flask_login import LoginManager

from config import Config  # your config.py at project root

# ——————————————————————————————————————————————
# initialize extensions
db       = SQLAlchemy()
migrate  = Migrate()
bootstrap = Bootstrap4()
login    = LoginManager()
login.login_view = 'auth.login'         # where @login_required redirects
login.login_message_category = 'info'   # flash category for the login prompt
# ——————————————————————————————————————————————

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # ensure the instance folder exists (so SQLite can create the file)
    os.makedirs(app.instance_path, exist_ok=True)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    login.init_app(app)

    # register blueprints
    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main.routes import main_bp
    app.register_blueprint(main_bp)

    return app

# ——————————————————————————————————————————————
# Flask‐Login user_loader
# this tells Flask‐Login how to load a user from the session ID
@login.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))
# ——————————————————————————————————————————————