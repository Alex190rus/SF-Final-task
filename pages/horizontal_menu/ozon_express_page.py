import pytest


class Ozon_Express():

    def __init__(self, driver):
        self.driver = driver

    def get_ozon_express(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Доставка за час')]")