import pytest


class Certificates():

    def __init__(self, driver):
        self.driver = driver

    def get_certificates(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Присмотритесь')]")