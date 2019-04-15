from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from blueprints.page.views import page

app = Flask(__name__)
app.config.from_pyfile("../config/settings.py")
app.config.from_pyfile("../instance/settings.py", silent=True)

app.register_blueprint(page)

login_manager = LoginManager()

login_manager.init_app(app)
db = SQLAlchemy(app)
Bootstrap(app)


@login_manager.user_loader
def load_user(user_id):
    from user import User  # Resolve circular imports

    return User.get(user_id)


app.run('0.0.0.0', 8000)
