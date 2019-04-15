from flask import Flask
from extensions import login_manager, db, bootstrap
from blueprints.page.views import page
from blueprints.user.views import user
from blueprints.user.models.models import User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("../config/settings.py")
    app.config.from_pyfile("../instance/settings.py", silent=True)

    app.register_blueprint(page)
    app.register_blueprint(user)

    extensions(app)

    return app


def extensions(app):
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)



@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', 8000)
