import pytest


class Protection_Against_Hacking():

    def __init__(self, driver):
        self.driver = driver

    def get_protection_against_hacking(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Проверьте адрес сайта')]")