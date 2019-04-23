from movierate.app import create_app

import pytest
from movierate.extensions import db as _db
from movierate.blueprints.user.models.user import User


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup flask test app

    :return: Flask app
    """
    test_db = 'sqlite:///ratemovies_test.db'
    settings = {
        'DEBUG': False,
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': test_db
    }

    _app = create_app(test_config=settings)

    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    return app.test_client()


@pytest.fixture(scope='session')
def db(app):

    _db.drop_all()
    _db.create_all()

    params = {
        'email': 'admin@local.host',
        'password': 'password',
    }

    admin = User(**params)

    _db.session.add(admin)
    _db.session.commit()

    return _db
