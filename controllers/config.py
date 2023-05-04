from RPA.Robocorp.WorkItems import WorkItems

wi = WorkItems()
wi.get_input_work_item()

default_work_item = {
          "search_phrase": "python",
          "news_sections": ["ARTS", "BOOKS"],
          "month_amount": 3
        }

SEARCH_PHRASE = wi.get_work_item_variable(
    'search_phrase', default_work_item['search_phrase'])
news_sections = wi.get_work_item_variable(
    'news_sections', default_work_item['news_sections'])
NEWS_SECTIONS = [section.upper() for section in news_sections]
MONTH_AMOUNT = wi.get_work_item_variable(
    'month_amount', default_work_item['month_amount'])
