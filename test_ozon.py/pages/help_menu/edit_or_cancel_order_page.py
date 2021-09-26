import pytest


class Edit_Or_Cancel_Order():

    def __init__(self, driver):
        self.driver = driver

    def get_edit_or_cancel_order(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Отменить заказ')]")