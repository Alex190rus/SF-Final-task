import pytest


class Delivery_Abroad():

    def __init__(self, driver):
        self.driver = driver

    def get_delivery_abroad(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Австралия')]")