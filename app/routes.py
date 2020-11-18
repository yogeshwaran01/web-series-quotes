from random import choice, choices

from flask import jsonify

from app import app
from data.breaking_bad import BREAKING_BAD_QUOTES
from data.dark import DARK_QUOTES
from data.game_of_thrones import GAME_OF_THRONES_QUOTES
from data.money_heist import MONEY_HEIST_QUOTES

SERIES = ["breakingbad", "dark", "gameofthrones", "moneyheist"]
ALL = BREAKING_BAD_QUOTES + DARK_QUOTES + GAME_OF_THRONES_QUOTES + MONEY_HEIST_QUOTES
SERIES_URL = [
    "https://web-series-quotes.herokuapp.com/breakingbad",
    "https://web-series-quotes.herokuapp.com/dark",
    "https://web-series-quotes.herokuapp.com/gameofthrones",
    "https://web-series-quotes.herokuapp.com/moneyheist"
]


def finder(query):
    if query == "breakingbad":
        return BREAKING_BAD_QUOTES
    elif query == "dark":
        return DARK_QUOTES
    elif query == "gameofthrones":
        return GAME_OF_THRONES_QUOTES
    elif query == "moneyheist":
        return MONEY_HEIST_QUOTES
    else:
        pass
    
def get_by_id(query, id_):
    result_ = None
    for i in finder(query):
        if i['id'] == id_:
            result_ = i
    return result_
        

@app.errorhandler(404)
def not_found(error):
    return jsonify([{"error": "404 Not Found"}]), 404


@app.route("/")
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
