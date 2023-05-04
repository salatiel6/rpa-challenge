import urllib.request
import re
import os

from RPA.Browser.Selenium import Selenium
from .config import NEWS_SECTIONS
from .feats import feats


class ArticleScraper:
    def __init__(self):
        try:
            # Create a Selenium object to control the web browser
            self.browser_lib = Selenium()

        except Exception as e:
            print(f"An error occurred: {e}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser_lib.close_browser()

    def open_the_website(self, url):
        try:
            self.browser_lib.open_available_browser(url)

            # The following lines set the width and height of the browser
            # window to 1920x1080 pixels.
            window_width = 1920
            window_height = 1080
            self.browser_lib.set_window_size(window_width, window_height)
        except Exception as e:
            print(f"An error occurred while opening the website: {e}")

    def input_search(self, search_phrase):
        try:
            # Find the search button on the website and wait
            # until it is visible
            search_button_loc = "css:button[data-test-id='search-button']"
            self.browser_lib.wait_until_element_is_visible(search_button_loc)

            # Click on the search button
            self.browser_lib.click_element(search_button_loc)

            # Find the search box on the website and input the search phrase
            # stored in the class variable
            search_box_loc = "css:input[data-testid='search-input']"
            search_box = self.browser_lib.find_element(search_box_loc)
            self.browser_lib.input_text(search_box, search_phrase)

            # Press the ENTER key to start the search
            self.browser_lib.press_keys(search_box, "ENTER")
        except Exception as e:
            print(f"An error occurred while inputting the search phrase: {e}")

    def select_sections(self):
        try:
            # Find the section element
            section_loc = "css:div[data-testid='section']"
            section = self.browser_lib.find_element(section_loc)

            # Find the section button element inside the section element
            section_button_loc = \
                "css:button[data-testid='search-multiselect-button']"
            section_button = self.get_child_element(
                section_button_loc, section)

            # Click the section button to expand the section list
            section_button.click()

            # Find the section list element
            section_list_loc = \
                "css:ul[data-testid='multi-select-dropdown-list']"
            section_list = self.browser_lib.find_element(section_list_loc)

            # Find all the section items in the section list
            section_items_loc = \
                "css:input[data-testid='DropdownLabelCheckbox']"
            section_items = self.get_child_element(
                section_items_loc, section_list, True)

            # For each section item that belongs to the news sections, click it
            [
                self.browser_lib.click_element(section_item)
                for section_item in section_items
                if section_item.get_attribute("value").split("|")[0].upper()
                in NEWS_SECTIONS
            ]
        except Exception as e:
            print(f"An error occurred while selecting sections: {e}")

    def sort_by(self, sort_option):
        try:
            # Find the sort dropdown element and click it
            sort_dropdown_loc = "css:select[data-testid='SearchForm-sortBy']"
            sort_dropdown = self.browser_lib.find_element(sort_dropdown_loc)
            sort_dropdown.click()

            # Find the specified sort option and click it
            newest_option_loc = f"css:option[value='{sort_option}']"
            newest_option = self.get_child_element(
                newest_option_loc, sort_dropdown)
            newest_option.click()
        except Exception as e:
            print(f"An error occurred while sorting: {e}")

    def get_articles(self):
        try:
            # Find the list of articles and its items
            articles_list_loc = "css:ol[data-testid='search-results']"
            articles_list = self.browser_lib.find_element(articles_list_loc)
            articles_items_loc = "css:li[data-testid='search-bodega-result']"
            articles_items = self.get_child_element(
                articles_items_loc, articles_list, True)

            # Define a list of valid months based on the number of months
            # defined in the configuration
            months = feats.define_months()

            # Locate the elements for the article date,
            # title, description, and picture
            article_date_loc = "css:span[data-testid='todays-date']"
            article_title_loc = "css:h4"
            article_description_loc = "css:p.css-16nhkrn"
            article_picture_loc = "css:img"

            # Initialize an empty list to store the articles
            articles = []

            # Loop through each article item
            # and extract its relevant information
            for article_item in articles_items:
                # Extract the month of the article publication date and check
                # if it's a valid month
                article_date = self.get_child_element(
                    article_date_loc, article_item)
                article_month = article_date.get_attribute(
                    "aria-label").upper().split(" ")[0]

                if article_month in months:
                    # Extract the title, description,
                    # and picture of the article
                    title = self.get_child_element(
                        article_title_loc, article_item).text
                    date = article_date.get_attribute("aria-label")
                    description = self.get_child_element(
                        article_description_loc, article_item).text
                    picture_src = self.get_child_element(
                        article_picture_loc, article_item).get_attribute("src")

                    # Download the picture
                    picture = picture_src.split("?")[0].split("/")[-1]

                    # Get the directory path of this file
                    module_dir = os.path.dirname(__file__)

                    # Create a directory for output files if it doesn't exist
                    filedir = os.path.join(module_dir, '', 'outputs')
                    if not os.path.exists(filedir):
                        os.makedirs(filedir)

                    # Save the workbook to a file
                    file_path = os.path.join(filedir, picture)

                    urllib.request.urlretrieve(picture_src, file_path)

                    # Count the number of occurrences of the search phrase
                    # in the title and description
                    count = title.count(
                        'search_phrase') + description.count('search_phrase')

                    # Check if the title or description
                    # contains a dollar amount
                    regex = re.compile(
                        r"^\$?\d+(,\d{3})*(\.\d+)?( USD)?$|^\d+ dollars?$")
                    has_money = True if regex.match(title) \
                        or regex.match(description) else False

                    # Append the article information to the articles list
                    articles.append({
                        'title': title,
                        'date': date,
                        'description': description,
                        'picture': picture,
                        'count': count,
                        'has_money': has_money
                    })

            return articles
        except Exception as e:
            print(f"An error occurred while getting articles: {e}")

    def get_child_element(self, child_element_loc, parent_element,
                          multiple_element=False):
        try:
            # check if multiple_element flag is set to True
            if multiple_element:
                # find all child elements with given locator
                # under the given parent element
                element = self.browser_lib.find_elements(
                    locator=child_element_loc,
                    parent=parent_element
                )
            else:
                # find a single child element with given locator
                # under the given parent element
                element = self.browser_lib.find_element(
                    locator=child_element_loc,
                    parent=parent_element
                )

            # return the found child element(s)
            return element
        except ValueError as ve:
            print(f"ValueError: {ve}")

        except Exception as e:
            print(f"An error occurred while getting the chilld element: {e}")
