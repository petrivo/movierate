from flask import Flask
from movierate.extensions import login_manager, db
from movierate.blueprints.page.views import page
from movierate.blueprints.user.views import user
from movierate.blueprints.user.models.user import User


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(page)
    app.register_blueprint(user)

    extensions(app)

    register_errorhandlers(app)

    return app


def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return str(error_code)
        # return render_template("{0}.html".format(error_code)), error_code

    for errcode in [404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def extensions(app):
    login_manager.init_app(app)
    db.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
