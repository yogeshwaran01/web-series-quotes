import io
from typing import Callable

from fastapi.responses import Response

import requests

from PIL import Image, ImageDraw, ImageFont, ImageColor

COLORS = list(ImageColor.colormap.keys())

def image_response(image: Image.new) -> Response:
    buffer = io.BytesIO()
    image.save(buffer, format='jpeg')
    res = Response(buffer.getvalue(), media_type='image/jpeg')
    return res

def create_background(x: int=3600, y: int=2400, color: str='white') -> Image.new:
    return Image.new("RGB", (x, y), color=color)

class ImageProcessor:
    """
    Class Processes the image and make response
    """

    def __init__(self, image: Image.new, text: str, size: int, color: str):
        self.image = image
        self.font = ImageFont.truetype("font/LuxuriousRoman-Regular.ttf", size)
        self.text = self.wrap_text(text)
        self.color = color

    @classmethod
    def image_from_url(cls, url: str, text: str, size: int, color: str):
        res = requests.get(url, stream=True)
        res.raw.decode_content = True
        return cls(Image.open(res.raw), text, size, color)

    @classmethod
    def colored_background(cls, text: str, size: int, text_color: str, x: int=3600, y: int=2400, back_color: str='white'):
        
        return cls(Image.new("RGB", (x, y), color=back_color), text, size, text_color)

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
        if self.color in COLORS:
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
        return image_response(self.texted_image())
