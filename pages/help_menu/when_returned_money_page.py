import pytest


class When_Returned_Money():

    def __init__(self, driver):
        self.driver = driver

    def get_when_returned_money(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Куда вернутся деньги')]")