import pytest

from app import app


@pytest.fixture
def client():
    """ Initiation of Testing """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
