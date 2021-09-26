import pytest


class ElectronicsPage():

    def __init__(self, driver):
        self.driver = driver

    def get_electronics(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Электроника')]")