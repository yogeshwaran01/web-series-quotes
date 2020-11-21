import pytest
from flask import request

from app import app
from app.routes import SERIES_URL, get_by_id, SERIES, finder


@pytest.fixture
def client():
    """ Initiation of Testing """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


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


def test_quote_generator(client):
    """ Testcase for quote image generator with colored background """
    response = client.get("/generate/blank?fore=yellow&back=green&size=250")
    assert request.args["fore"] == "yellow"
    assert request.args["back"] == "green"
    assert request.args["size"] == "250"
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"


def test_quote_generator_with_in_build_images(client):
    """ Testcase for quote image generator with image background """
    response = client.get("/generate/moneyheist/2/image?src=dark&color=yellow&size=150")
    assert request.args["src"] == "dark"
    assert request.args["color"] == "yellow"
    assert request.args["size"] == "150"
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"


def test_quote_generator_with_user_image(client):
    """ Testcase for quote image generator with user image background """
    image = "https://www.gstatic.com/webp/gallery/3.png"
    response = client.get(
        f"/generate/moneyheist/5/image?src={image}&color=yellow&size=100"
    )
    assert request.args["src"] == image
    assert request.args["color"] == "yellow"
    assert request.args["size"] == "100"
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"


def test_blank(client):
    """ Testcase for quote image generator with colored background """
    response = client.get("/generate/blank")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"


def test_image(client):
    """ Test case for quote image generator with image background """
    response = client.get("/generate/image?text=hello+world")
    assert request.args["text"] == "hello world"
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"
