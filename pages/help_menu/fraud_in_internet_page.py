import pytest


class Fraud_In_Internet():

    def __init__(self, driver):
        self.driver = driver

    def get_fraud_in_internet(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Фишинг')]")