from RPA.Robocorp.WorkItems import WorkItems

wi = WorkItems()
wi.get_input_work_item()

SEARCH_PHRASE = wi.get_work_item_variable('search_phrase')
NEWS_SECTIONS = wi.get_work_item_variable('news_sections')
MONTH_AMOUNT = wi.get_work_item_variable('month_amount')
