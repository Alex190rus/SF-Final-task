import pytest


class Koupons():

    def __init__(self, driver):
        self.driver = driver

    def get_koupons(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Как применить')]")