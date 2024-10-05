#!/usr/bin/env python3

from flask import Flask
from config import Config
from app.v1.extensions import jwt, socketio, elasticsearch

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
   
    # Initialize extensions
    jwt.init_app(app)
    socketio.init_app(app)
    elasticsearch.init_app(app)
   
    # Register blueprints
    from app.v1.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')
   
    return app
