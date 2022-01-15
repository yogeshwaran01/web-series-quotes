from fastapi import FastAPI

app = FastAPI()

from .routes import quote
from .routes import image

app.include_router(quote.router)
app.include_router(image.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
