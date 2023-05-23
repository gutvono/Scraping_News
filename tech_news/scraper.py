from typing import List
from parsel import Selector
from re import findall
from tech_news.database import create_news
import requests
import time


# Faz a requisição HTTP ao site e retorna o conteúdo HTML.
def fetch(url: str) -> str:
    time.sleep(1)
    try:
        response = requests.get(
            url,
            headers={'user-agent': 'Fake user-agent'},
            timeout=3
        )
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Utiliza a biblioteca Parsel para obter as URLs das páginas.
def scrape_updates(html_content: str) -> List[str]:
    urls_list = Selector(html_content)
    return urls_list.css('h2.entry-title a::attr(href)').getall()


# Obtém a URL da próxima página.
def scrape_next_page_link(html_content: str) -> str or None:
    page_content = Selector(html_content)
    if page_content:
        return page_content.css('a.next.page-numbers::attr(href)').get()
    return None


# Preenche um dicionário com as informações encontradas na página.
def scrape_news(html_content):
    html = Selector(html_content)

    return {
        "url": html.css('head > link[rel=canonical]::attr(href)').get(),
        "title": html.css('h1.entry-title::text').get().strip(),
        "timestamp": html.css('li.meta-date::text').get(),
        "writer": html.css('span.author a::text').get(),
        "reading_time": int(findall(
            r"\d+", html.css('li.meta-reading-time::text').get())[0]),
        "summary": ''.join(html.css(
            ".entry-content > p:first-of-type *::text").getall()).strip(),
        "category": html.css('span.label::text').get()
    }


# Responsável por realizar o processo de scraping e armazenar o conteúdo
# encontrado no banco de dados MongoDB
def get_tech_news(amount):
    news_list = []
    next_page = "https://blog.betrybe.com/"
    html_content = fetch(next_page)
    news_url_list = scrape_updates(html_content)
    while len(news_url_list) < amount:
        next_page = scrape_next_page_link(html_content)
        if next_page is not None:
            html_content = fetch(next_page)
            news_url_list.extend(scrape_updates(html_content))
    for news_url in news_url_list[:amount]:
        news_list.append(scrape_news(fetch(news_url)))
    create_news(news_list)
    return news_list
