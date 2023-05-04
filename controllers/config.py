from RPA.Robocorp.WorkItems import WorkItems

wi = WorkItems()
input_work_item = wi.get_input_work_item()

SEARCH_PHRASE = input_work_item["search_phrase"]
NEWS_SECTIONS = input_work_item["news_sections"]
MONTH_AMOUNT = input_work_item["month_amount"]
