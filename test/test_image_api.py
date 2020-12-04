from flask import request

from test import client
from app.routes import IN_BUILD_IMAGES, SUPPORTED_COLORS


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
    for image in IN_BUILD_IMAGES:
        response = client.get(
            f"/generate/moneyheist/2/image?src={image}&color=yellow&size=150"
        )
        assert request.args["src"] == image
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


def test_color(client):
    """ Test case for supported colors """
    response = client.get("/colors")
    assert SUPPORTED_COLORS == response.get_json()


def test_in_buld_images(client):
    """ Test case for buid-in images """
    response = client.get("/images")
    assert IN_BUILD_IMAGES == response.get_json()


def test_size_of_image(client):
    """ Test case for size of the image """
    response = client.get(
        "/generate/blank?fore=black&back=white&text=Black&x=1000&y=1000&size=200"
    )
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"
    assert request.args["x"] == "1000"
    assert request.args["y"] == "1000"
