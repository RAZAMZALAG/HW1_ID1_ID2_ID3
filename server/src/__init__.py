"""
__init__.py

This module defines the Flask app factory function `create_app`.
It sets up the Flask application, configures it, and registers the main blueprints.
"""
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'super-secret-key'

    # register blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
