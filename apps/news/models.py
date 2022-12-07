from pydantic import BaseModel, validator


class ModelNews(BaseModel):
    news_id: int
    title: str
    description: str = ''

    @validator('title')
    def title_so_long(cls, value):
        if len(value) > 20:
            raise ValueError("so long")
        return value

    @validator('title')
    def oleg_validator(cls, value):
        if "oleg" in value.lower():
            raise ValueError("Attention Oleg detected!")
        return value


class SimpleModel(BaseModel):
    name: str


class PriceModel(BaseModel):
    usd: float
    eth: float
    eur: float


class MarketDataModel(BaseModel):
    current_price: PriceModel


class BitcoinModel(BaseModel):
    symbol: str
    name: str
    genesis_date: str
    market_data: MarketDataModel
