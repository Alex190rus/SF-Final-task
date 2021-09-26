import pytest


class Regular_Delivery():

    def __init__(self, driver):
        self.driver = driver

    def get_regular_delivery(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Как оформить регулярную доставку')]")