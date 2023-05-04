# import time
import os

# from controllers import ArticleScraper, FileHandler, SEARCH_PHRASE
from RPA.Robocorp.WorkItems import WorkItems


def main():
    # with ArticleScraper() as article_scrapper:
    #     url = "https://www.nytimes.com"
    #     article_scrapper.open_the_website(url)
    #     article_scrapper.input_search(SEARCH_PHRASE)
    #     article_scrapper.select_sections()
    #     article_scrapper.sort_by("newest")
    #     time.sleep(3)
    #     articles = article_scrapper.get_articles()
    #
    # file_handler = FileHandler()
    # file_handler.save_to_excel(articles, "articles.xlsx")

    filename = "work_items.txt"

    # Get the directory path of this file
    module_dir = os.path.dirname(__file__)

    # Create a directory for output files if it doesn't exist
    filedir = os.path.join(module_dir, './controllers', 'outputs')
    if not os.path.exists(filedir):
        os.makedirs(filedir)

    # Get the full path of the output file
    file_path = os.path.join(filedir, filename)

    wi = WorkItems()
    wi.get_input_work_item()
    customers = wi.get_work_item_variable("customers")
    for customer in customers:
        with open(file_path, 'w') as file:
            file.write(customer)


if __name__ == "__main__":
    main()
