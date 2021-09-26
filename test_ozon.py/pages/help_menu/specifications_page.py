import pytest


class Specifications():

    def __init__(self, driver):
        self.driver = driver

    def get_specifications(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Товара нет в наличии')]")