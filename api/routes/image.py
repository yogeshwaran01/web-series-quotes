import itertools
import random
from data import data
from fastapi import APIRouter, Query
from typing import Optional, Any
from pydantic import AnyUrl

from api.utils.generate_image import ImageProcessor, create_background, COLORS

router = APIRouter(prefix="/pic")


ALL_QUOTES = list(itertools.chain(*data.values()))
AVAILABLE_SERIES = list(data.keys())


def get_by_id(data: list[dict], id_: int) -> Any:

    result_ = None
    for i in data:
        if i["id"] == id_:
            result_ = i
    return result_


@router.get("/solid", tags=["Get Quotes with Colored backgroud"])
async def render_pic_colored_background(
    series: Optional[str] = Query(
        default=None,
        description=", ".join(AVAILABLE_SERIES),
    ),
    id: Optional[int] = Query(
        default=None, description="Get quote with id <code>Series name required </code>"
    ),
    background_color: Optional[str] = Query(
        default="black", description="Backgroud color name"
    ),
    text_color: Optional[str] = Query(default="white", description="Color of the Text"),
    text_size: Optional[int] = Query(default=200, description="Size of the Text"),
    x: Optional[int] = Query(default=3600, description="Width of the image"),
    y: Optional[int] = Query(default=2400, description="Height of the image"),
):
    if text_color not in COLORS:
        text_color = "white"

    if background_color not in COLORS:
        text_color = "black"

    if series in AVAILABLE_SERIES:
        text_data = get_by_id(data.get(series), id) or random.choice(data.get(series))
    else:
        text_data = random.choice(ALL_QUOTES)

    background_pic = create_background(x, y, background_color)
    text = text_data["quote"]
    image = ImageProcessor(background_pic, text, text_size, text_color)

    return image.response()


@router.get("/image", tags=["Get Quotes with Image backgroud"])
async def render_pic_with_image_background(
    series: Optional[str] = Query(
        default=None,
        description=", ".join(AVAILABLE_SERIES),
    ),
    id: Optional[int] = Query(
        default=None, description="Get quote with id <code>Series name required </code>"
    ),
    background_img_url: Optional[AnyUrl] = Query(
        default="https://www.gstatic.com/webp/gallery/3.png",
        description="Backgroud image URL",
    ),
    text_color: Optional[str] = Query(default="black", description="Color of the Text"),
    text_size: Optional[int] = Query(default=200, description="Size of the Text"),
):
    if text_color not in COLORS:
        text_color = "white"

    if series in AVAILABLE_SERIES:
        text_data = get_by_id(data.get(series), id) or random.choice(data.get(series))
    else:
        text_data = random.choice(ALL_QUOTES)

    text = text_data["quote"]
    image = ImageProcessor.image_from_url(
        background_img_url, text, text_size, text_color
    )

    return image.response()


@router.get("/custom", tags=["Generate images with custom text"])
async def render_pic_colored_background_custom_text(
    text: Optional[str] = Query(
        default="Hello World",
        description="Any text",
    ),
    background_color: Optional[str] = Query(
        default="white", description="Backgroud color name"
    ),
    image_url: Optional[AnyUrl] = Query(
        default=None, description="Background image url"
    ),
    text_color: Optional[str] = Query(default="black", description="Color of the Text"),
    text_size: Optional[int] = Query(default=200, description="Size of the Text"),
    x: Optional[int] = Query(default=3600, description="Width of the image"),
    y: Optional[int] = Query(default=2400, description="Height of the image"),
):

    if text_color not in COLORS:
        text_color = "black"

    if background_color not in COLORS:
        background_color = "white"

    if image_url:
        try:
            return ImageProcessor.image_from_url(image_url, text, text_size, text_color).response()
        except:  # noqa: E722
            return {"msg": "invalid url"}

    return ImageProcessor.colored_background(
        text, text_size, text_color, x, y, background_color
    ).response()
