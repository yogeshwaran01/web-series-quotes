import random
import itertools
from typing import Any, Optional

from fastapi import APIRouter, Query

from data import data

router = APIRouter(prefix="/quote")

ALL_QUOTES = list(itertools.chain(*data.values()))
AVAILABLE_SERIES = list(data.keys())


def get_by_id(data: list[dict], id_: int) -> Any:

    result_ = {
        "message": f"Series has only {len(data)} Quotes Don't use more than this"
    }
    for i in data:
        if i["id"] == id_:
            result_ = i
    return result_


@router.get("/", tags=["Get Quotes"], description="Get a random or particular quote(s)")
async def get_quote(
    series: Optional[str] = Query(
        default=None,
        description=", ".join(AVAILABLE_SERIES),
    ),
    count: Optional[int] = Query(
        default=None, description="Count of random quotes to be returned"
    ),
    id: Optional[int] = Query(
        default=None, description="Get quote with id <code>Series name required </code>"
    ),
    all: Optional[bool] = Query(
        default=None, description="True if all quote of series to be returned"
    ),
) -> Any:
    if count is None:
        count = 1
    if series:
        if series in AVAILABLE_SERIES:
            if id:
                return get_by_id(data.get(series), id_=id)
            if all:
                return data.get(series)
            return random.choices(data.get(series), k=count)
        else:
            return {"message": "series not found", "series": AVAILABLE_SERIES}
    return random.choices(ALL_QUOTES, k=count)
