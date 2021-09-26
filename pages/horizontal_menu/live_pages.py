import pytest


class LivePage():

    def __init__(self, driver):
        self.driver = driver

    def get_live(self):
        return pytest.driver.find_element_by_xpath('//*[contains(text(), "Перейти на страницу")]')