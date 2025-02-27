from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()  # ✅ Define mongo first

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)  # ✅ Initialize after Flask app

    from app.routes import user_routes  
    app.register_blueprint(user_routes)

    return app
