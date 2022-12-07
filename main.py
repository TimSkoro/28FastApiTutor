from fastapi import FastAPI

from apps.news.router import news
from apps.other.router import other

app = FastAPI()
app.include_router(news)
app.include_router(other)

