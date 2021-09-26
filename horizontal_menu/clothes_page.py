import pytest


class ClothesPage():

    def __init__(self, driver):
        self.driver = driver

    def get_clothes(self):
        return pytest.driver.find_element_by_xpath('//*[contains(text(), "Женщинам")]')