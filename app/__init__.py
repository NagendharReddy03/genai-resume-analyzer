from flask import Flask
from flask_bootstrap5 import Bootstrap5

bootstrap = Bootstrap5()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
    Bootstrap5(app)
    bootstrap.init_app(app)
    
    # Import after app creation to avoid circular imports
    from app.main.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app