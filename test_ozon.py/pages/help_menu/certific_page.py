import pytest


class Сertific():

    def __init__(self, driver):
        self.driver = driver

    def get_certific(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Подарочные сертификаты')]")