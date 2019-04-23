from flask import Flask
from movierate.extensions import login_manager, db
from movierate.blueprints.page.views import page
from movierate.blueprints.user.views import user
from movierate.blueprints.user.models.models import User


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(page)
    app.register_blueprint(user)

    extensions(app)

    return app


def extensions(app):
    login_manager.init_app(app)
    db.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
