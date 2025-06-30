from flask import Flask
from app.models import db
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
import cloudinary

csrf = CSRFProtect()
migrate = Migrate()

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    project_folder = os.path.abspath(os.path.join(base_dir))

    app = Flask(
        __name__,
        template_folder=os.path.join(project_folder, '..', 'templates'),
        static_folder=os.path.join(project_folder, '..', 'static')
    )

    # Load .env only if NOT running on Render
    if os.getenv("RENDER") is None:
        load_dotenv(os.path.join(base_dir, '..', '.env'))

    # MySQL Database configuration
    mysql_name = os.getenv('MYSQL_USER')
    mysql_password = quote_plus(os.getenv('MYSQL_PASSWORD'))
    mysql_host = os.getenv('MYSQL_HOST')
    mysql_port = os.getenv('MYSQL_PORT', '3306')
    mysql_db = os.getenv('MY_DATABASE')

    # TEMP: Debug print — REMOVE after checking
    print(f"MYSQL_PORT being used: {mysql_port}")

    # Cloudinary configuration
    cloudinary.config(
        cloud_name=os.getenv('CLOUD_NAME'),
        api_key=os.getenv('API_KEY'),
        api_secret=os.getenv('API_SECRET')
    )

    # Flask config
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{mysql_name}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}?charset=utf8mb4"
    )
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_secret_fallback')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ALLOWED_EXTENSION'] = {'JPG', 'jpeg', 'png'}

    # Add pool_recycle and pool_pre_ping to avoid lost connection errors
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_recycle': 280,
        'pool_pre_ping': True
    }

    # Init extensions
    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.routes.land_routes import land_bp
    app.register_blueprint(land_bp)

    return app