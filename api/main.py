from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from .routes import quote
from .routes import image
from api.utils.generate_image import COLORS

app = FastAPI(
    title="Web Series Quotes Api",
    description="Quotes of various web series with image generating feature",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(quote.router)
app.include_router(image.router)


@app.get("/all", tags=["Get all Quotes"])
async def all_quotes():
    return quote.ALL_QUOTES


@app.get("/series", tags=["Get all Available series"])
async def all_available_series():
    return quote.AVAILABLE_SERIES


@app.get("/colors", tags=["Get all Colors for image Generation"])
async def all_available_colors():
    return COLORS


@app.get("/", tags=["Others"])
async def root():
    return RedirectResponse(url="/docs")
