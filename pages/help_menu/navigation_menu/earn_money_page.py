import pytest


class Earn_money():

    def __init__(self, driver):
        self.driver = driver

    def get_earn_money(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Мы поможем')]")