import pytest


class Business():

    def __init__(self, driver):
        self.driver = driver

    def get_business(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Как начать делать покупки?')]")