import requests
from fastapi import APIRouter

from apps.news.models import BitcoinModel

coingecko_url = 'https://api.coingecko.com/api/v3/coins/bitcoin'

other = APIRouter(prefix='/other', tags=['other'])


@other.get("/")
def root():
    return {"message": "Hello World"}


@other.get('/bitcoin')
def bitcoin_info():
    data = requests.get(coingecko_url).json()
    return BitcoinModel(**data)


@other.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
