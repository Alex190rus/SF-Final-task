import pytest


class Receipts_And_Documents():

    def __init__(self, driver):
        self.driver = driver

    def get_receipts_and_documents(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Где взять чек')]")