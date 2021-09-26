import pytest


class How_To_Place_An_Order():

    def __init__(self, driver):
        self.driver = driver

    def get_how_to_place_an_order(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'На сайте')]")
