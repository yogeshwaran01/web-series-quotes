from random import choice, choices
from typing import Any, Optional

from flask import jsonify, request

from app import app
from data.breaking_bad import BREAKING_BAD_QUOTES
from data.dark import DARK_QUOTES
from data.game_of_thrones import GAME_OF_THRONES_QUOTES
from data.money_heist import MONEY_HEIST_QUOTES
from .image_processing import colored_back, image_back, in_build_image_back

SERIES = ["breakingbad", "dark", "gameofthrones", "moneyheist"]
ALL = BREAKING_BAD_QUOTES + DARK_QUOTES + GAME_OF_THRONES_QUOTES + MONEY_HEIST_QUOTES
SERIES_URL = [
    "https://web-series-quotes.herokuapp.com/breakingbad",
    "https://web-series-quotes.herokuapp.com/dark",
    "https://web-series-quotes.herokuapp.com/gameofthrones",
    "https://web-series-quotes.herokuapp.com/moneyheist",
]

IN_BUILD_IMAGES = ["breakingbad", "dark", "gameofthrones", "moneyheist"]


def finder(query: str) -> list:
    """
    Function find the user query and return requires list
    """
    if query == "breakingbad":
        return BREAKING_BAD_QUOTES
    elif query == "dark":
        return DARK_QUOTES
    elif query == "gameofthrones":
        return GAME_OF_THRONES_QUOTES
    elif query == "moneyheist":
        return MONEY_HEIST_QUOTES
    else:
        return []


def get_by_id(query: str, id_: int) -> Optional[Any]:
    """
    Function search the data by id
    """
    result_ = None
    for i in finder(query):
        if i["id"] == id_:
            result_ = i
    return result_


@app.errorhandler(404)
def not_found(error):
    return jsonify([{"error": "404 Not Found"}]), 404


@app.route("/")
@app.route("/api")
def index():
    return jsonify(SERIES_URL)


@app.route("/random/<series>/")
@app.route("/random/<series>")
def random_(series):
    if series in SERIES:
        return jsonify(choice(finder(series)))
    else:
        return not_found(404)


@app.route("/random/<series>/<int:random_number>/")
@app.route("/random/<series>/<int:random_number>")
def random_choice(series, random_number):
    if series in SERIES:
        return jsonify(choices(finder(series), k=random_number))
    else:
        return not_found(404)


@app.route("/random/")
@app.route("/random")
def random_all():
    return jsonify(choice(ALL))


@app.route("/random/<int:random_number>/")
@app.route("/random/<int:random_number>")
def random_all_choice(random_number):
    return jsonify(choices(ALL, k=random_number))


@app.route("/<series>/")
@app.route("/<series>")
def get_quote_all(series):
    return jsonify(finder(series))


@app.route("/<series>/<int:id_>/")
@app.route("/<series>/<int:id_>")
def by_id(series, id_):
    return jsonify(get_by_id(series, id_))


@app.route("/generate/<series>/<int:id_>/blank")
def generate_quotes_blank(series, id_):
    text = get_by_id(series, id_)["quote"]
    back = request.args.get("back")
    fore = request.args.get("fore")
    try:
        size = int(request.args.get("size"))
    except TypeError:
        size = 300
    return colored_back(back, text, fore, size)


@app.route("/generate/<series>/<int:id_>/image")
def generate_quotes_image(series, id_):
    text = get_by_id(series, id_)["quote"]
    path = request.args.get("src")
    color = request.args.get("color")
    try:
        size = int(request.args.get("size"))
    except TypeError:
        size = 300
    if path is None:
        return colored_back(b_color="white", text=text, f_color="black", font_size=size)
    if path in IN_BUILD_IMAGES:
        return in_build_image_back(path, text, color, font_size=size)
    return image_back(path, text, color, font_size=size)


@app.route("/generate/blank")
def generate_blank():
    text = request.args.get("text")
    if text is None:
        text = "Add Text in Query"
    back = request.args.get("back")
    fore = request.args.get("fore")
    try:
        size = int(request.args.get("size"))
    except TypeError:
        size = 300
    return colored_back(back, text, fore, size)


@app.route("/generate/image")
def generate_image():
    text = request.args.get("text")
    if text is None:
        text = "Add Text in Query"
    path = request.args.get("src")
    color = request.args.get("color")
    try:
        size = int(request.args.get("size"))
    except TypeError:
        size = 300
    if path is None:
        return colored_back(b_color="white", text=text, f_color="black", font_size=size)
    if path in SERIES:
        return in_build_image_back(path, text, color, font_size=size)
    return image_back(path, text, color, font_size=size)
