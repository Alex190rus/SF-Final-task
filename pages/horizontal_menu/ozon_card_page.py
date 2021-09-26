import pytest


class Ozon_Card():

    def __init__(self, driver):
        self.driver = driver

    def get_ozon_card(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Ozon.Card')]")