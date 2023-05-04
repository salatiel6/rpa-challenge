from RPA.Robocorp.WorkItems import WorkItems

wi = WorkItems()
input_work_item = wi.get_input_work_item()

SEARCH_PHRASE = input_work_item.get("search_phrase")
NEWS_SECTIONS = input_work_item.get("news_sections")
MONTH_AMOUNT = input_work_item.get("month_amount")
