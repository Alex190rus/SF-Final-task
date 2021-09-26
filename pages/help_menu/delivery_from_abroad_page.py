import pytest


class Delivery_From_Abroad():

    def __init__(self, driver):
        self.driver = driver

    def get_delivery_from_abroad(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Срок хранения')]")