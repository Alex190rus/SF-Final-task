import pytest


class Order_Status():

    def __init__(self, driver):
        self.driver = driver

    def get_order_status(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Что означает статус заказа')]")