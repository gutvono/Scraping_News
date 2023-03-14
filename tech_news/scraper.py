from typing import List
from parsel import Selector
import requests
import time


# Requisito 1
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


# Requisito 2
def scrape_updates(html_content: str) -> List[str]:
    urls_list = Selector(html_content)
    return urls_list.css('h2.entry-title a::attr(href)').getall()


# Requisito 3
def scrape_next_page_link(html_content: str) -> str or None:
    page_content = Selector(html_content)
    if page_content:
        return page_content.css('a.next.page-numbers::attr(href)').get()
    return None


# Requisito 4
def scrape_news(html_content):
    html = Selector(html_content)

    return {
        "url": html.css('a.cs-overlay-link::attr(href)').get(),
        "title": html.css('h1.entry-title::text').get(),
        "timestamp": html.css('li.meta-date::text').get(),
        "writer": html.css('span.author a::text').get(),
        "reading_time": int(html.css('li.meta-reading-time i::text').get()[0]),
        "summary": html.css('div.entry-content p *::text').get(),
        "category": html.css('span.label::text').get()
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
