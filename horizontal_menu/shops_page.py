import pytest


class ShopPage():

    def __init__(self, driver):
        self.driver = driver

    def get_shops(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Книги')]")