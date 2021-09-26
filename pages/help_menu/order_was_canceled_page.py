import pytest


class Order_Was_Canceled():

    def __init__(self, driver):
        self.driver = driver

    def get_order_was_canceled(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Мой заказ отменили')]")