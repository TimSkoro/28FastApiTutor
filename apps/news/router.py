from fastapi import APIRouter
from pydantic import BaseModel

from apps.common.constant import NEWS_DATA
from apps.common.data_types import BlogType
# from apps.news.models import ModelNews, SimpleModel

news = APIRouter(prefix='/news', tags=['news'])


class ModelNews(BaseModel):
    news_id: int
    title: str
    description: str = ''


@news.post('/create')
def create_news(to_chto_so_fronta_prishlo: ModelNews):
    print(f"Try to post item: {to_chto_so_fronta_prishlo}")
    return {"result": "kind off created"}


@news.get('/by_category/{news_type}')
def get_news(news_type: BlogType):
    return {"result": NEWS_DATA[news_type]}


@news.get('/end')
def endpoint():
    return {"result": "kind off get"}


@news.post('/end')
def endpoint():
    return {"result": "kind off post"}
