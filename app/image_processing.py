import io
from typing import Callable

import requests

from PIL import Image, ImageDraw, ImageFont, ImageColor, UnidentifiedImageError
from flask import make_response

SUPPORTED_COLORS = list(ImageColor.colormap.keys())


def create_background(color: str, x: int, y: int) -> Image.new:
    """
    Function Create image of given color and size
    """
    if color in SUPPORTED_COLORS:
        img = Image.new("RGB", (x, y), color=color)
    else:
        img = Image.new("RGB", (x, y), color="white")
    return img


class ImageProcessing:
    """
    Class Processes the image and make response
    """

    def __init__(self, filepath: str, text: str, size: int, color: str):
        try:
            self.image = Image.open(filepath)
        except AttributeError:
            self.image = filepath
        except FileNotFoundError:
            try:
                res = requests.get(filepath, stream=True)
                res.raw.decode_content = True
                self.image = Image.open(res.raw)
            except UnidentifiedImageError:
                self.image = create_background("black", 3000, 2005)
        self.font = ImageFont.truetype("font/AlternateGotNo2D.otf", size)
        self.text = self.wrap_text(text)
        self.color = color

    def wrap_text(self, text: str) -> str:
        new_text = ""
        new_sentence = ""
        for word in text.split(" "):
            delim = " " if new_sentence != "" else ""
            new_sentence = new_sentence + delim + word
            if len(new_sentence) > 25:
                new_text += "\n" + new_sentence
                new_sentence = ""
        new_text += "\n" + new_sentence
        return new_text

    def texted_image(self) -> Image.Image:
        texted_img = self.image
        darw = ImageDraw.Draw(texted_img)
        w, h = texted_img.size
        x, y = w / 2, h / 2
        w_, h_ = darw.multiline_textsize(self.text, font=self.font, spacing=3)
        x -= w_ / 2
        y -= h_ / 2
        if self.color in SUPPORTED_COLORS:
            darw.multiline_text(
                align="center",
                xy=(x, y),
                text=self.text,
                fill=self.color,
                font=self.font,
            )
        else:
            darw.multiline_text(
                align="center", xy=(x, y), text=self.text, fill="black", font=self.font
            )
        return texted_img

    def response(self) -> Callable:
        buffer = io.BytesIO()
        self.texted_image().save(buffer, format="png")
        buffer.seek(0)
        res = make_response(buffer.getvalue())
        res.mimetype = "image/png"
        return res
