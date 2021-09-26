import pytest


class Payment_Error():

    def __init__(self, driver):
        self.driver = driver

    def get_payment_error(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'ЮMoney')]")