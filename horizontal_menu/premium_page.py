import pytest


class Premium():

    def __init__(self, driver):
        self.driver = driver

    def get_premium(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Premium баллы')]")