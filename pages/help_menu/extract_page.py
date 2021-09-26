import pytest


class Extract():

    def __init__(self, driver):
        self.driver = driver

    def get_extract(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Выписку')]")