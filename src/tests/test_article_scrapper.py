from pytest import fixture
from ..controllers import ArticleScraper


class TestArticle:
    @fixture
    def scraper(self):
        with ArticleScraper() as scraper:
            scraper.open_the_website("https://www.nytimes.com/")
            yield scraper

    def test_open_the_website(self, scraper):
        assert scraper.browser_lib.get_location() == "https://www.nytimes.com/"

    def test_input_search(self, scraper):
        scraper.input_search("Coronavirus")
        assert "search" in scraper.browser_lib.get_location()

    def test_select_sections(self, scraper):
        scraper.input_search("python")
        scraper.select_sections()
        section_items = scraper.browser_lib.find_elements(
            "css:input[type='checkbox'][data-testid='checkbox-label']")
        selected_sections = [
            item.get_attribute("value").upper()
            for item in section_items if item.is_selected()]
        assert all(
            section in selected_sections for section in ["ARTS", "BOOKS"])
