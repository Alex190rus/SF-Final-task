import pytest


class Discount():

    def __init__(self, driver):
        self.driver = driver

    def get_discount(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Распродажа')]")