import time

from controllers import ArticleScraper, FileHandler, SEARCH_PHRASE


def main():
    with ArticleScraper() as article_scrapper:
        url = "https://www.nytimes.com"
        article_scrapper.open_the_website(url)
        article_scrapper.input_search(SEARCH_PHRASE)
        article_scrapper.select_sections()
        article_scrapper.sort_by("newest")
        time.sleep(3)
        articles = article_scrapper.get_articles()

    if articles:
        file_handler = FileHandler()
        file_handler.save_to_excel(articles, "articles.xlsx")
    else:
        raise ValueError("No articles found")


if __name__ == "__main__":
    main()
