"""
Using Pydantic to validate the request and response schemas.
"""
from pydantic import BaseModel, HttpUrl


class ShortenRequest(BaseModel):
    url: HttpUrl


class ShortenResponse(BaseModel):
    short_url: str
    short_code: str
