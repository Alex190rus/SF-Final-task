import pytest


class Pick_Up_Order():

    def __init__(self, driver):
        self.driver = driver

    def get_pick_up_order(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Постамат')]")