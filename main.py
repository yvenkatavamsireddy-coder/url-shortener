from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from datetime import datetime, timedelta

from database import (
    create_table,
    save_url,
    get_url,
    get_existing_url,
    short_code_exists
)

from schemas import URLRequest
from utils import generate_short_code

app = FastAPI()

create_table()


@app.get("/")
def home():
    return {"message": "URL Shortener API"}


@app.post("/shorten")
def shorten_url(data: URLRequest):

    existing = get_existing_url(data.url)

    if existing:

        short_code = existing[0]
        expires_at = existing[1]

        expiry_date = datetime.strptime(
            expires_at,
            "%Y-%m-%d"
        )

        if datetime.now() <= expiry_date:
            return {
                "short_code": short_code,
                "short_url": f"http://127.0.0.1:8000/{short_code}",
                "expires_at": expires_at,
                "message": "Existing short URL reused"
            }

    short_code = generate_short_code()

    while short_code_exists(short_code):
        short_code = generate_short_code()

    expiry_date = (
        datetime.now() +
        timedelta(days=30)
    ).strftime("%Y-%m-%d")

    save_url(
        short_code,
        data.url,
        expiry_date
    )

    return {
        "short_code": short_code,
        "short_url": f"http://127.0.0.1:8000/{short_code}",
        "expires_at": expiry_date,
        "message": "New short URL created"
    }


@app.get("/{short_code}")
def redirect_url(short_code: str):

    result = get_url(short_code)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="URL not found"
        )

    original_url = result[0]
    expires_at = result[1]

    expiry_date = datetime.strptime(
        expires_at,
        "%Y-%m-%d"
    )

    if datetime.now() > expiry_date:
        raise HTTPException(
            status_code=410,
            detail="URL expired"
        )

    return RedirectResponse(original_url)