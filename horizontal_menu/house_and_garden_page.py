import pytest


class House_And_Garden():

    def __init__(self, driver):
        self.driver = driver

    def get_house_and_garden(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Посуда')]")