import pytest


class Shiping_Cost():

    def __init__(self, driver):
        self.driver = driver

    def get_shiping_cost(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Ozon Premium')]")