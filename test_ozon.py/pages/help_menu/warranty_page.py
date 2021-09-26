import pytest


class Warranty():

    def __init__(self, driver):
        self.driver = driver

    def get_warranty(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Какие нужны документы')]")