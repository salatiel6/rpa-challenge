import time
from ..controllers import ArticleScraper, SEARCH_PHRASE


def test_article_scraper():
    with ArticleScraper() as article_scraper:
        url = "https://www.nytimes.com"
        article_scraper.open_the_website(url)
        article_scraper.input_search(SEARCH_PHRASE)
        article_scraper.select_sections()
        article_scraper.sort_by("newest")
        time.sleep(3)
        articles = article_scraper.get_articles()
        assert len(articles) > 0
