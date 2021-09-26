import pytest


class Ozon_Points():

    def __init__(self, driver):
        self.driver = driver

    def get_ozon_points(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Баллы Ozon')]")