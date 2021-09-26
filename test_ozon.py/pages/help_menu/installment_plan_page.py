import pytest


class Installment_Plan():

    def __init__(self, driver):
        self.driver = driver

    def get_installment_plan(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Получите лимит')]")