import pytest


class Referral():

    def __init__(self, driver):
        self.driver = driver

    def get_referral(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), '300 баллов')]")