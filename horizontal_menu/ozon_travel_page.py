import pytest


class Ozon_Travel():

    def __init__(self, driver):
        self.driver = driver

    def get_ozon_travel(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Авиабилеты')]")