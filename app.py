import os

from flask import Flask
from flask_cors import CORS
from config import Config
from models import db

from routes.song_routes import song_bp
from routes.user_routes import user_bp
from routes.health_routes import health_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)

    # Register blueprints
    app.register_blueprint(song_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(health_bp)

    return app


app = create_app()


if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 5000))

    app.run(host=host, port=port, debug=True)

