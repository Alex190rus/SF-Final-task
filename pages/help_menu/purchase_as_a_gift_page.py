import pytest


class Purchase_As_A_Gift():

    def __init__(self, driver):
        self.driver = driver

    def get_purchase_as_a_gift(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Как оформить подарок')]")