import pytest


class TOP_Fashion():

    def __init__(self, driver):
        self.driver = driver

    def get_top_fashion(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Трикотаж')]")