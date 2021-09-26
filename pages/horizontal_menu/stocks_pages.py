import pytest


class StocksPage():

    def __init__(self, driver):
        self.driver = driver

    def get_stocks(self):
        return pytest.driver.find_element_by_xpath('//*[contains(text(), "Акции и спецпредложения")]')