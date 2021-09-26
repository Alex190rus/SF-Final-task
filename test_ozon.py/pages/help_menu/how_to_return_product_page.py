import pytest


class How_To_Return_Product():

    def __init__(self, driver):
        self.driver = driver

    def get_how_to_return_product(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Передайте курьеру')]")