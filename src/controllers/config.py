import os
import configparser

config = configparser.ConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_file_path)

SEARCH_PHRASE = config.get('DEFAULT', 'search_phrase')
NEWS_SECTIONS = config.get('DEFAULT', 'news_sections').split(',')
MONTH_AMOUNT = config.getint('DEFAULT', 'month_amount')
