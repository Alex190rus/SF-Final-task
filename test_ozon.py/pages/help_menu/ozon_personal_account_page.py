import pytest


class Ozon_Personal_Account():

    def __init__(self, driver):
        self.driver = driver

    def get_ozon_personal_account(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Как начисляются Ozon Бонусы')]")