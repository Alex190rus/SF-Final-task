import pytest


class Fitting():

    def __init__(self, driver):
        self.driver = driver

    def get_fitting(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Пункт выдачи')]")