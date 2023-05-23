from tech_news.database import search_news
from datetime import datetime


# Busca notícias no banco de dados que foram "raspadas" do site pelo título.
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for news in news_list:
        result.append((news['title'], news['url']))
    return result


# Busca notícias no banco de dados pela data.
def search_by_date(date):
    try:
        news_list = search_news({'timestamp': datetime.strptime(
            date, '%Y-%m-%d').strftime("%d/%m/%Y")})
        result = []
        for news in news_list:
            result.append((news['title'], news['url']))
        return result
    except ValueError:
        raise ValueError('Data inválida')


# Busca notícias no banco de dados pela categoria.
def search_by_category(category):
    news_list = search_news({
        "category": {"$regex": category, "$options": "i"}})
    result = []
    for news in news_list:
        result.append((news['title'], news['url']))
    return result
