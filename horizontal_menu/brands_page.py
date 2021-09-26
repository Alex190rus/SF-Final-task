import pytest


class BrandsPage():

    def __init__(self, driver):
        self.driver = driver

    def get_brands(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Все бренды')]")