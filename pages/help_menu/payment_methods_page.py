import pytest


class Payment_Methods():

    def __init__(self, driver):
        self.driver = driver

    def get_payment_methods(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Банковской картой')]")