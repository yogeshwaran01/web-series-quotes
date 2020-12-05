from flask import request

from test import client
from app import app
from app.routes import SERIES_URL, SERIES
from app.routes import get_by_id, finder


def test_home_page(client):
    """ Testcase for home url """
    response = client.get("/")
    response = client.get("/api")
    assert SERIES_URL == response.get_json()
    assert SERIES_URL == response.get_json()


def test_series(client):
    """ Testcase for all quotes in series """
    for i in SERIES:
        response = client.get(f"/{i}")
        assert finder(i) == response.get_json()


def test_random_series(client):
    """ Testcase for random quotes in series """
    for i in SERIES:
        response = client.get(f"/random/{i}")
        assert response.get_json() in finder(i)


def test_series_by_id(client):
    """ Testcase for get quotes by series id """
    for i in SERIES:
        response = client.get(f"/{i}/10")
        assert response.get_json() == get_by_id(i, 10)
