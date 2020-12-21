from random import choice, choices

from flask import jsonify, request, redirect, render_template

from app import app
from .image_processing import SUPPORTED_COLORS
from .utils import ALL, IN_BUILD_IMAGES, SERIES, SERIES_URL
from .utils import colored_back, image_back, in_build_image_back
from .utils import get_by_id, finder


@app.errorhandler(404)
def not_found(error):
    return jsonify([{"error": "404 Not Found"}]), 404


@app.route("/")
def home1():
    return render_template("index1.html", colors=SUPPORTED_COLORS, series=SERIES)


@app.route("/api")
def index():
    return jsonify(SERIES_URL)


@app.route("/help")
@app.route("/docs")
def help():
    return redirect("https://github.com/yogeshwaran01/web-series-quotes")


@app.route("/colors")
def color_supported():
    return jsonify(SUPPORTED_COLORS)


@app.route("/images")
def in_build_image():
    return jsonify(IN_BUILD_IMAGES)


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
    x = request.args.get("x")
    y = request.args.get("y")
    try:
        size = int(request.args.get("size"))
    except TypeError:
        size = 300
    if x and y is not None:
        return colored_back(back, text, fore, size, x=int(x), y=int(y))
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
    x = request.args.get("x")
    y = request.args.get("y")
    try:
        size = int(request.args.get("size"))
    except TypeError:
        size = 300
    if x and y is not None:
        return colored_back(back, text, fore, size, x=int(x), y=int(y))
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


@app.errorhandler(500)
def internal_server_error(e):
    """ Handling internal_server_error 500 error """
    return jsonify({"message": "Invaild url paramters"})


@app.errorhandler(404)
def page_not_used(e):
    """ Handling internal_server_error 500 error """
    return jsonify({"message": "Page not found"})
