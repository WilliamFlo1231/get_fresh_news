import logging
from RPA.Browser.Selenium import Selenium

class AP:
    def __init__(self, CONFIG) -> None:
        self.CONFIG = CONFIG
        self.browser = Selenium()
    
    def navigate_to_news(self):
        self.browser.open_browser(self.CONFIG.AP.url)
        self.browser.wait_until_element_is_visible(self.CONFIG.AP.search_button,
                                                   self.CONFIG.delays.medium)
        search_button = self.browser.find_element(self.CONFIG.AP.search_button)
        logging.info('Searching for phrase')
        search_button.click()

if __name__ == '__main__':
    import sys
    sys.path.append('../get_fresh_news')
    from utils.config import load_config
    c = load_config('./config.yaml')
    a = AP(c)
    a.navigate_to_news()
    ...