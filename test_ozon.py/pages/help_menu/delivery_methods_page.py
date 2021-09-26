import pytest


class Delivery_methods():

    def __init__(self, driver):
        self.driver = driver

    def get_delivery_methods(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Срок хранения')]")