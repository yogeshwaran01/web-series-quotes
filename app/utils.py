from typing import Any, Optional, Callable

from .image_processing import ImageProcessing
from .image_processing import create_background

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
    "https://web-series-quotes.herokuapp.com/moneyheist",
]
IN_BUILD_IMAGES = [
    "breakingbad",
    "dark",
    "gameofthrones",
    "moneyheist",
    "cardboard",
    "rainbowmountain",
    "joker",
]


def finder(query: str) -> Any:
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
        return BREAKING_BAD_QUOTES


def get_by_id(query: str, id_: int) -> Optional[Any]:
    """
    Function search the data by id
    """
    result_ = {
        "quote": f"Series {query} has only {len(finder(query))} Quotes Don't use more than this"
    }
    for i in finder(query):
        if i["id"] == id_:
            result_ = i
    return result_


def colored_back(
    b_color: str, text: str, f_color: str, font_size=300, x=3000, y=2005
) -> Callable:
    """
    Function return the response of text added image of given color
    """
    return ImageProcessing(
        create_background(b_color, x, y), text, size=font_size, color=f_color
    ).response()


def image_back(path: str, text: str, color: str, font_size=300) -> Callable:
    """
    Function return the response of text added given image
    """
    return ImageProcessing(path, text, size=font_size, color=color).response()


def in_build_image_back(name: str, text: str, color: str, font_size=300) -> Callable:
    """
    Function similar to image_back specially for build in images
    """
    return ImageProcessing(
        f"images/{name}.jpg", text, size=font_size, color=color
    ).response()
