from app import create_app

import pytest

@pytest.yield_fixture(scope='session')
def app():
    """
    Setup flask test app

    :return: Flask app
    """

    app = create_app(test_settings=settings)