import os
from dotenv import load_dotenv

load_dotenv()  # .env faylini yuklash

from flask import Flask
from config import Config
from extensions import db, login_manager, bcrypt, csrf


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return db.session.get(User, int(user_id))

    from routes.auth import auth
    from routes.main import main
    from routes.admin import admin

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(admin)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
