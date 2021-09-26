import pytest


class Delivery_Ozon_Express():

    def __init__(self, driver):
        self.driver = driver

    def get_delivery_ozon_express(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Что такое Ozon Express')]")