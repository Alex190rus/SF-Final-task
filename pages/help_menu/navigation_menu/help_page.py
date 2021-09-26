import pytest


class Help():

    def __init__(self, driver):
        self.driver = driver

    def get_help(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Мой заказ')]")